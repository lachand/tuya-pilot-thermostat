"""
Plateforme principale Climate pour Tuya Thermostat
"""
from __future__ import annotations
import logging
from typing import Any
from homeassistant.components.climate import ClimateEntity, ClimateEntityFeature, HVACMode
from homeassistant.const import ATTR_TEMPERATURE
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN, DP_MAP, MODES
from .entity import TuyaThermostatEntity

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    name = config_entry.title
    unique_id = config_entry.unique_id or config_entry.entry_id
    entity = TuyaThermostatClimate(coordinator, config_entry, unique_id, name)
    async_add_entities([entity])

class TuyaThermostatClimate(TuyaThermostatEntity, ClimateEntity):
    _attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT, HVACMode.AUTO]
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_min_temp = 5.0
    _attr_max_temp = 35.0

    def __init__(self, coordinator, config_entry, unique_id, name):
        super().__init__(coordinator, config_entry, unique_id, name)
        self._attr_name = name
        self._attr_unique_id = unique_id

    @property
    def current_temperature(self) -> float | None:
        return self.coordinator.data.temp_current

    @property
    def target_temperature(self) -> float | None:
        return self.coordinator.data.temp_set

    @property
    def hvac_mode(self) -> str:
        mode = self.coordinator.data.mode
        if mode == "off":
            return HVACMode.OFF
        if mode == "auto":
            return HVACMode.AUTO
        return HVACMode.HEAT

    async def async_set_temperature(self, **kwargs: Any) -> None:
        temp = kwargs.get(ATTR_TEMPERATURE)
        if temp is not None:
            dps = {str(DP_MAP["temp_set"]): int(temp * 10)}
            await self.coordinator.client.async_set(dps)
            await self.coordinator.async_request_refresh()

    async def async_set_hvac_mode(self, hvac_mode: str) -> None:
        mode_map = {
            HVACMode.OFF: "off",
            HVACMode.AUTO: "auto",
            HVACMode.HEAT: "heat",
        }
        dps = {str(DP_MAP["mode"]): mode_map.get(hvac_mode, "heat")}
        await self.coordinator.client.async_set(dps)
        await self.coordinator.async_request_refresh()
