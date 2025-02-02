import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from datetime import timedelta
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from homeassistant.helpers.typing import ConfigType
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass

from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_NAME,
    CONF_UNIQUE_ID
)

from .hargassner import HargassnerBridge

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(seconds=5)

PLATFORMS = [Platform.SENSOR]

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_NAME, default="Hargassner"): cv.string,
        vol.Optional(CONF_UNIQUE_ID, default="1"): cv.string,
    })
}, extra=vol.ALLOW_EXTRA
)


async def async_setup_entry(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.data[DOMAIN] = {}
    hass.data[DOMAIN][CONF_HOST] = config.data[CONF_HOST]
    hass.data[DOMAIN][CONF_NAME] = config.data[CONF_NAME]
    hass.data[DOMAIN][CONF_UNIQUE_ID] = config.data[CONF_UNIQUE_ID]

    # await hass.helpers.discovery.async_load_platform('sensor', DOMAIN, {}, config)

    await hass.config_entries.async_forward_entry_setups(config, PLATFORMS)

    return True
