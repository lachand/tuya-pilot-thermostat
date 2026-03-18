"""
Coordinator pour Tuya Thermostat (DataUpdateCoordinator)
"""
from __future__ import annotations

import logging
from datetime import timedelta
from typing import Any

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant

from .tuya_thermostat import TuyaThermostatClient, ThermostatState
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class TuyaThermostatCoordinator(DataUpdateCoordinator[ThermostatState]):
    def __init__(
        self,
        hass: HomeAssistant,
        client: TuyaThermostatClient,
        name: str,
        update_interval: timedelta = timedelta(seconds=30),
    ):
        super().__init__(
            hass,
            _LOGGER,
            name=name,
            update_interval=update_interval,
        )
        self.client = client

    async def _async_update_data(self) -> ThermostatState:
        try:
            return await self.client.async_status()
        except Exception as err:
            raise UpdateFailed(f"Erreur lors du polling thermostat Tuya: {err}")
