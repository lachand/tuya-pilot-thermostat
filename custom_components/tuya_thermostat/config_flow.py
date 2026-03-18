"""
Config flow et options flow pour Tuya Thermostat
"""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.data_entry_flow import FlowResult
from .const import DOMAIN

DEFAULT_PROTOCOL_VERSION = "3.3"
DEFAULT_SCAN_INTERVAL = 30

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required("name", default="Thermostat"): str,
    vol.Required("host"): str,
    vol.Required("device_id"): str,
    vol.Required("local_key"): str,
    vol.Optional("protocol_version", default=DEFAULT_PROTOCOL_VERSION): str,
})

STEP_OPTIONS_DATA_SCHEMA = vol.Schema({
    vol.Optional("scan_interval", default=DEFAULT_SCAN_INTERVAL): vol.All(int, vol.Range(min=5, max=600)),
    # Ajout d'autres options ici (features, limites, profil DP)
})

class TuyaThermostatConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow pour Tuya Thermostat."""
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None) -> FlowResult:
        errors = {}
        if user_input is not None:
            # Validation de la connexion au thermostat
            valid = await self._async_validate_connection(user_input)
            if valid:
                return self.async_create_entry(title=user_input["name"], data=user_input)
            errors["base"] = "cannot_connect"
        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    async def _async_validate_connection(self, data) -> bool:
        # Validation basique : tentative de connexion via tinytuya
        from .tuya_thermostat import TuyaThermostatClient
        try:
            client = TuyaThermostatClient(
                data["host"], data["device_id"], data["local_key"], data.get("protocol_version", DEFAULT_PROTOCOL_VERSION)
            )
            state = await client.async_status()
            return state.temp_current is not None
        except Exception:
            return False

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return TuyaThermostatOptionsFlowHandler(config_entry)

class TuyaThermostatOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self._config_entry = config_entry

    async def async_step_init(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        options = self._config_entry.options.copy()
        return self.async_show_form(
            step_id="init",
            data_schema=STEP_OPTIONS_DATA_SCHEMA,
            errors=errors,
        )
