"""
Binary sensors pour Tuya Thermostat (état chauffe, fenêtre, alarme)
"""
from homeassistant.components.binary_sensor import BinarySensorEntity
from .const import DOMAIN
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatBinarySensor(coordinator, config_entry, unique_id + "_heating", name + " Chauffe", "running_mode", "heating"),
        TuyaThermostatBinarySensor(coordinator, config_entry, unique_id + "_window", name + " Fenêtre ouverte", "window_state", True),
        TuyaThermostatBinarySensor(coordinator, config_entry, unique_id + "_fault", name + " Alarme", "fault", 1),
    ]
    async_add_entities(entities)

class TuyaThermostatBinarySensor(TuyaThermostatEntity, BinarySensorEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, attr, on_value):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_attr = attr
        self._attr_on_value = on_value

    @property
    def is_on(self):
        val = getattr(self.coordinator.data, self._attr_attr, None)
        return val == self._attr_on_value
