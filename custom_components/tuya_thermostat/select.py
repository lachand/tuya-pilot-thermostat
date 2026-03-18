"""
Selects pour Tuya Thermostat (unités, profils DP, modes avancés)
"""
from homeassistant.components.select import SelectEntity
from .const import DOMAIN, DP_MAP, MODES, MODES_MAP, MODES_MAP_REVERSE
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatSelect(coordinator, config_entry, unique_id + "_unit", name + " Unité", "temp_unit", DP_MAP["temp_unit"], ["c", "f"]),
        TuyaThermostatModeSelect(coordinator, config_entry, unique_id + "_mode", name + " Mode", DP_MAP["mode"]),
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


class TuyaThermostatModeSelect(TuyaThermostatEntity, SelectEntity):
    """Select avec labels FR mappés aux valeurs Tuya."""

    def __init__(self, coordinator, config_entry, unique_id, name, dp_id):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_dp_id = dp_id
        self._attr_options = MODES

    @property
    def current_option(self):
        tuya_val = self.coordinator.data.mode
        return MODES_MAP_REVERSE.get(tuya_val, tuya_val)

    async def async_select_option(self, option: str):
        tuya_val = MODES_MAP.get(option, option)
        await self.coordinator.client.async_set({str(self._attr_dp_id): tuya_val})
        await self.coordinator.async_request_refresh()
