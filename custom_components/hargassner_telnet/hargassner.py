import asyncio
import logging;
from datetime import datetime, timedelta
import xml.etree.ElementTree as xml
from homeassistant.helpers.entity import Entity
from .const import BRIDGE_STATE_OK, BRIDGE_STATE_DISCONNECTED, BRIDGE_TIMEOUT
from .telegram import _MSG_TELEGRAM, _FIELD_CONFIG

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=5)

class HargassnerParameter:
    def __init__(self, key, index, unit):
        self._key = key
        self._index = index
        self._value = None
        self._unit = unit

    def __str__(self):
        if self.value() and self.unit():
            return self.description() + ": " + self.value() + " " + self.unit()
        elif self.value():
            return self.description() + " : " + self.value()
        else:
            return self.description() + " : unknown"

    def key(self):
        return self._key

    def hasFieldConfig(self):
        fc = _FIELD_CONFIG.get(self.key(), self.key())

        return fc is not None and type(fc) != str

    def fieldConfig(self):
        fc = _FIELD_CONFIG.get(self.key(), self.key())

        if fc is None:
            return self._key

        return fc

    def index(self):
        return self._index

    def value(self):
        fc = self.fieldConfig()

        if type(fc) == str:
            return self._value

        return fc.convertValue(self._value)

    def unit(self):
        return self._unit

    def description(self):
        fc = self.fieldConfig()

        if type(fc) == str:
            return fc

        return fc.getName()


class HargassnerAnalogueParameter(HargassnerParameter):

    def __init__(self, key, index, unit):
        super().__init__(key, index, unit)

    def initializeFromMessage(self, msg):
        self._value = msg[self._index]

class HargassnerDigitalParameter(HargassnerParameter):

    def __init__(self, key, index, bitmask):
        super().__init__(key, index, None)
        self._bitmask = bitmask

    def initializeFromMessage(self, msg):
        try:
            self._value = (str)(((int)(msg[self._index], 32) & self._bitmask) > 0)
        except Exception:
            self._value = None

SCAN_INTERVAL = timedelta(seconds=5)


class HargassnerBridge(Entity):
    def __init__(self, hostIP, name, uniqueId):
        self._hostIP = hostIP
        self._connectionOK = False
        self._reader = None
        self._writer = None
        self._latestUpdate = None
        self._paramData = {}
        self._expectedMsgLength = 0
        self._missedMsgs = 0
        self._errorLog = ""
        self._infoLog = ""
        self._name = name + " Verbindung"
        self._unique_id = uniqueId
        self.setMessageFormat(_MSG_TELEGRAM)

    def setMessageFormat(self, msgFormat):
        if not msgFormat.startswith("<DAQPRJ>"):
            _LOGGER.error("HargassnerBridge.setMessageFormat(): Message template does not start with '<DAQPRJ>'.\n")
            return False

        # get xml from raw message format

        root = xml.fromstring(msgFormat)

        # parse analogue message format

        index = 0
        analog = root.find("ANALOG")
        for channel in analog.findall("CHANNEL"):
            uniqueName = (str)(channel.get("name"))

            nameCount = 1

            while (
                uniqueName in self._paramData
            ):  # in case parameter name is duplicate, add a counter to make it unique
                nameCount += 1
                uniqueName = (str)(channel.get("name")) + "_" + str(nameCount)

            unit = channel.get("unit")

            if unit is not None:
                strUnit = (str)(unit)
            else:
                strUnit = None  # in case parameter has no unit, do not use string conversion but set explicitly to None

            # add parameter to parsed list
            
            # chId = (int)(channel.get("id")) # not used cause of dop

            self._paramData[uniqueName] = HargassnerAnalogueParameter(
                uniqueName, index, strUnit
            )

            index += 1

        # calculate raw digital data offset

        ofsDigital = len(self._paramData)

        # parse digital message format

        lenDigital = 0
        digital = root.find("DIGITAL")
        for channel in digital.findall("CHANNEL"):
            self._paramData[(str)(channel.get("name"))] = HargassnerDigitalParameter(
                (str)(channel.get("name")),
                ofsDigital + (int)(channel.get("id")),
                1 << (int)(channel.get("bit")),
            )
            lenDigital = (int)(
                channel.get("id")
            ) + 1  # assuming that channel ids are increasing

        # calculate full expected length

        self._expectedMsgLength = ofsDigital + lenDigital
        self._infoLog += (
            "HargassnerBridge.setMessageFormat(): successfully parsed "
            + (str)(self._expectedMsgLength)
            + " elements.\n"
        )

        return True

    async def async_will_remove_from_hass(self) -> None:
        """Close connection."""
        print("Hargassner Telnet async_will_remove_from_hass")
        await super().async_will_remove_from_hass()
        if self._writer:
            try:
                self._writer.close()
                await self._writer.wait_closed()
            except Exception:
                pass

    async def async_update(self):
        if not self._connectionOK:
            _LOGGER.info("HargassnerBridge.async_update(): Opening connection...")
            try:
                if self._writer:
                    self._writer.close()
                    await self._writer.wait_closed()

                self._reader, self._writer = await asyncio.wait_for(
                    asyncio.open_connection(self._hostIP, 23), timeout=BRIDGE_TIMEOUT
                )
                _LOGGER.info("HargassnerBridge.async_update(): Opened connection")
                self._connectionOK = True
            except Exception as e:
                _LOGGER.error("HargassnerBridge.async_update(): Error opening connection ("
                    + repr(e)
                    + ")\n")
                return

        try:
            msgReceived = False
            data = await asyncio.wait_for(
                self._reader.readline(), timeout=BRIDGE_TIMEOUT
            )
            line = data.decode().strip()
            msg = line.split()[1:]  # remove first field "pm"
            msglen = len(msg)

            _LOGGER.info("HargassnerBridge: message received (len " + str(msglen) + ")\n")
            # print(line)

            if msglen != self._expectedMsgLength:
                raise Exception("received", msglen, ", expected", self._expectedMsgLength)

            for param in self._paramData.values():
                param.initializeFromMessage(msg)                    
                # print(param)

            self._latestUpdate = datetime.now()
            msgReceived = True
            self._missedMsgs = 0

            if not msgReceived:
                _LOGGER.warning("HargassnerBridge._update(): Received message has unexpected length.\n")
                self._missedMsgs += 1
                if self._missedMsgs > 10:
                    self._connectionOK = False  # reconnect if too many errors
                    _LOGGER.error("HargassnerBridge._update(): Received message has unexpected length\n")

        except Exception as e:
            self._connectionOK = False

            _LOGGER.error("HargassnerBridge.async_update(): Telnet connection error ("
                + repr(e)
                + ")\n")

            # print(repr(e))
            return

    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return self._unique_id + "_Connection"

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return True

    @property
    def state(self) -> str | None:
        if self._connectionOK:
            return BRIDGE_STATE_OK
        else:
            return BRIDGE_STATE_DISCONNECTED

    @property
    def icon(self):
        """Return an icon for the sensor in the GUI."""
        if self._connectionOK:
            return "mdi:network-outline"
        else:
            return "mdi:network-off-outline"

    def getUniqueIdBase(self):
        return self._unique_id

    def getValue(self, paramName):
        param = self._paramData.get(paramName)
        if param == None:
            _LOGGER.error(
                "HargassnerBridge.getValue(): Parameter key "
                + paramName
                + " not known.\n"
            )
            return None
        return param.value()

    def getUnit(self, paramName):
        param = self._paramData.get(paramName)
        if param == None:
            _LOGGER.error(
                "HargassnerBridge.getUnit(): Parameter key "
                + paramName
                + " not known.\n"
            )
            return None
        return param.unit()

    def data(self):
        return self._paramData

    def latestUpdateTime(self):
        return self._latestUpdate

    def getErrorLog(self):
        log = self._errorLog
        self._errorLog = ""
        return log

    def getInfoLog(self):
        log = self._infoLog
        self._infoLog = ""
        return log
    