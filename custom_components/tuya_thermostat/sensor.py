"""
Capteurs pour Tuya Thermostat (température, puissance, etc.)
"""
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import UnitOfTemperature, UnitOfPower
from .const import DOMAIN, DP_MAP
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatSensor(coordinator, config_entry, unique_id + "_temp", name + " Température", "temp_current", UnitOfTemperature.CELSIUS),
        TuyaThermostatSensor(coordinator, config_entry, unique_id + "_power", name + " Puissance", "average_power", UnitOfPower.WATT),
    ]
    async_add_entities(entities)

class TuyaThermostatSensor(TuyaThermostatEntity, SensorEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, attr, unit):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_native_unit_of_measurement = unit
        self._attr_state_class = "measurement"
        self._attr_attr = attr

    @property
    def native_value(self):
        return getattr(self.coordinator.data, self._attr_attr, None)
