# Copie du fichier __init__.py depuis l'ancien emplacement
"""
Setup de l'intégration Tuya Thermostat
"""
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up via configuration.yaml (non supporté)."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Tuya Thermostat depuis une ConfigEntry."""
    hass.data.setdefault(DOMAIN, {})
    # Le reste de l'initialisation se fait dans les plateformes
    await hass.config_entries.async_forward_entry_setups(
        entry, ["climate", "sensor", "binary_sensor", "switch", "number", "select"]
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload une ConfigEntry."""
    unload_ok = all(
        await asyncio.gather(*[
            hass.config_entries.async_forward_entry_unload(entry, platform)
            for platform in ("climate", "sensor", "binary_sensor", "switch", "number", "select")
        ])
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
