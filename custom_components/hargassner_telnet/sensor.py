from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_NAME,
    CONF_UNIQUE_ID,
    BRIDGE_STATE_OK,
)
from datetime import timedelta
from .hargassner import HargassnerBridge

async def async_setup_entry(
    hass, config, async_add_entities
) -> None:
    """Set up the sensor platform."""
    host = hass.data[DOMAIN][CONF_HOST]
    name = hass.data[DOMAIN][CONF_NAME]
    uniqueId = hass.data[DOMAIN][CONF_UNIQUE_ID]
    bridge = HargassnerBridge(host, name, uniqueId)

    entities = [bridge]
    for p in bridge.data().values():
        if p.hasFieldConfig():
            entities.append(HargassnerSensor(bridge, name + " " + p.description(), p.key()))

    async_add_entities(entities)


class HargassnerSensor(SensorEntity):
    """Representation of a Sensor."""

    def __init__(self, bridge, description, paramName, icon=None):
        """Initialize the sensor."""
        self._value = None
        self._bridge = bridge
        self._description = description
        self._paramName = paramName
        self._icon = icon
        self._unique_id = bridge.getUniqueIdBase()
        self._unit = bridge.getUnit(paramName)
        self._stateClass = None
        self._deviceClass = None
        self._suggested_display_precision = None

        if self._unit == "A" or self._unit == "mA":
            self._deviceClass = SensorDeviceClass.CURRENT
            self._suggested_display_precision = 0
        elif self._unit == "V" or self._unit == "mV":
            self._deviceClass = SensorDeviceClass.VOLTAGE
            self._suggested_display_precision = 0
        elif self._unit == "W" or self._unit == "mW":
            self._deviceClass = SensorDeviceClass.POWER
            self._suggested_display_precision = 0
        elif self._unit == "kg":
            self._deviceClass = SensorDeviceClass.WEIGHT
            self._suggested_display_precision = 0
        elif self._unit == "mm":
            self._deviceClass = SensorDeviceClass.DISTANCE
            self._suggested_display_precision = 0
        elif self._unit == "Min":
            self._deviceClass = SensorDeviceClass.DURATION
            self._suggested_display_precision = 0
        elif self._unit == "°C":
            self._deviceClass = SensorDeviceClass.TEMPERATURE
            self._suggested_display_precision = 1
            

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._description

    @property
    def device_class(self):
        """Return the state of the sensor."""
        return self._deviceClass

    @property
    def state_class(self):
        """Return the state of the sensor."""
        return self._stateClass

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._value

    @property
    def native_unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit

    @property
    def suggested_display_precision(self):
        """Return the display precision of the sensor."""
        return self._suggested_display_precision

    @property
    def icon(self):
        """Return an icon for the sensor in the GUI."""
        return self._icon

    @property
    def available(self):
        if self._bridge.state == BRIDGE_STATE_OK:
            return True
        else:
            return False

    async def async_update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self._value = self._bridge.getValue(self._paramName)

    @property
    def unique_id(self):
        """Return the unique id of the sensor."""
        return self._unique_id + self._paramName
