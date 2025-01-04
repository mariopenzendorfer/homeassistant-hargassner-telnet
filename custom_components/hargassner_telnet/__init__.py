import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType


from .const import (
    DOMAIN,
    CONF_HOST,
    CONF_NAME,
    CONF_UNIQUE_ID
)


CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_NAME, default="Hargassner"): cv.string,
        vol.Optional(CONF_UNIQUE_ID, default="1"): cv.string,
    })
}, extra=vol.ALLOW_EXTRA
)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    hass.data[DOMAIN] = {}
    hass.data[DOMAIN][CONF_HOST] = config[DOMAIN].get(CONF_HOST)
    hass.data[DOMAIN][CONF_NAME] = config[DOMAIN].get(CONF_NAME)
    hass.data[DOMAIN][CONF_UNIQUE_ID] = config[DOMAIN].get(CONF_UNIQUE_ID)

    await hass.helpers.discovery.async_load_platform('sensor', DOMAIN, {}, config)

    return True
