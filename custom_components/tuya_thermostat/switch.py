"""
Switches pour Tuya Thermostat (verrouillage enfant, boost)
"""
from homeassistant.components.switch import SwitchEntity
from .const import DOMAIN, DP_MAP
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatSwitch(coordinator, config_entry, unique_id + "_child_lock", name + " Verrou enfant", "child_lock", DP_MAP["child_lock"]),
    ]
    async_add_entities(entities)

class TuyaThermostatSwitch(TuyaThermostatEntity, SwitchEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, attr, dp_id):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_attr = attr
        self._attr_dp_id = dp_id

    @property
    def is_on(self):
        return getattr(self.coordinator.data, self._attr_attr, None)

    async def async_turn_on(self, **kwargs):
        await self.coordinator.client.async_set({str(self._attr_dp_id): True})
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs):
        await self.coordinator.client.async_set({str(self._attr_dp_id): False})
        await self.coordinator.async_request_refresh()
