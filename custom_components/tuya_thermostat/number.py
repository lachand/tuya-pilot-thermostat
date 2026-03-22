"""
Numbers pour Tuya Thermostat (limites, boost, vacances)
"""
from homeassistant.components.number import NumberEntity, NumberDeviceClass
from homeassistant.const import UnitOfTemperature, UnitOfTime
from .const import DOMAIN, DP_MAP
from .entity import TuyaThermostatEntity

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entities = [
        TuyaThermostatNumber(coordinator, config_entry, unique_id + "_upper_temp", name + " Limite haute", "upper_temp", DP_MAP["upper_temp"], 15, 35, 0.5, UnitOfTemperature.CELSIUS, NumberDeviceClass.TEMPERATURE),
        TuyaThermostatNumber(coordinator, config_entry, unique_id + "_lower_temp", name + " Limite basse", "lower_temp", DP_MAP["lower_temp"], 5, 25, 0.5, UnitOfTemperature.CELSIUS, NumberDeviceClass.TEMPERATURE),
        TuyaThermostatNumber(coordinator, config_entry, unique_id + "_boost", name + " Boost", "boost_duration", DP_MAP["boost_duration"], 0, 120, 5, UnitOfTime.MINUTES, None),
        TuyaThermostatNumber(coordinator, config_entry, unique_id + "_holiday", name + " Vacances", "vacation_duration", DP_MAP["vacation_duration"], 0, 30, 1, UnitOfTime.DAYS, None),
    ]
    async_add_entities(entities)

class TuyaThermostatNumber(TuyaThermostatEntity, NumberEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, attr, dp_id, min_value, max_value, step, unit, device_class):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_attr = attr
        self._attr_dp_id = dp_id
        self._attr_native_min_value = min_value
        self._attr_native_max_value = max_value
        self._attr_native_step = step
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class

    @property
    def native_value(self):
        return getattr(self.coordinator.data, self._attr_attr, None)

    async def async_set_native_value(self, value):
        await self.coordinator.client.async_set({str(self._attr_dp_id): value})
        await self.coordinator.async_request_refresh()
