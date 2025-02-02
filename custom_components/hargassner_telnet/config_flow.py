from homeassistant import config_entries
import voluptuous as vol
from .const import(
    DOMAIN,
    CONF_HOST,
    CONF_NAME,
    CONF_UNIQUE_ID
) 


class HargassnerTelnetConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        return self.async_show_form(
            step_id="host", data_schema=vol.Schema({vol.Required(CONF_HOST): str, vol.Required(CONF_NAME, default="Hargassner"): str})
        )

    async def async_step_host(self, user_input=None):
        configName = f"{user_input[CONF_NAME]} ({user_input[CONF_HOST]})"
        return self.async_create_entry(
            title=configName,
            data= {
                CONF_HOST: user_input[CONF_HOST],
                CONF_NAME: user_input[CONF_NAME],
                CONF_UNIQUE_ID: configName,
            }
        )
