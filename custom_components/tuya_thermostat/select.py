"""
Selects pour Tuya Thermostat (unités, profils DP, modes avancés)
"""
from homeassistant.components.select import SelectEntity
from .const import DOMAIN, DP_MAP, MODES
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatSelect(coordinator, config_entry, unique_id + "_unit", name + " Unité", "temp_unit", DP_MAP["temp_unit"], ["c", "f"]),
        TuyaThermostatSelect(coordinator, config_entry, unique_id + "_mode", name + " Mode avancé", "mode", DP_MAP["mode"], MODES),
    ]
    async_add_entities(entities)

class TuyaThermostatSelect(TuyaThermostatEntity, SelectEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, attr, dp_id, options):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_attr = attr
        self._attr_dp_id = dp_id
        self._attr_options = options

    @property
    def current_option(self):
        return getattr(self.coordinator.data, self._attr_attr, None)

    async def async_select_option(self, option: str):
        await self.coordinator.client.async_set({str(self._attr_dp_id): option})
        await self.coordinator.async_request_refresh()
