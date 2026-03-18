# Copie du fichier __init__.py depuis l'ancien emplacement
"""
Setup de l'intégration Tuya Thermostat
"""
import logging
from datetime import timedelta
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN
from .tuya_thermostat import TuyaThermostatClient
from .coordinator import TuyaThermostatCoordinator

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up via configuration.yaml (non supporté)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Tuya Thermostat depuis une ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})

    client = TuyaThermostatClient(
        entry.data["host"],
        entry.data["device_id"],
        entry.data["local_key"],
        entry.data.get("protocol_version", "3.3"),
    )
    scan_interval = entry.options.get("scan_interval", 30)
    coordinator = TuyaThermostatCoordinator(
        hass, client, entry.title, timedelta(seconds=scan_interval)
    )
    await coordinator.async_config_entry_first_refresh()
    hass.data[DOMAIN][entry.entry_id] = {"coordinator": coordinator}

    await hass.config_entries.async_forward_entry_setups(
        entry, ["climate", "sensor", "binary_sensor", "switch", "number", "select"]
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload une ConfigEntry."""
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, ["climate", "sensor", "binary_sensor", "switch", "number", "select"]
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
