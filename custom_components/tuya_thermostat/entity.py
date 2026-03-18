"""
Classe de base TuyaThermostatEntity
"""
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, MANUFACTURER, ATTR_CARD_ROLE, ATTR_CARD_TOKEN

class TuyaThermostatEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry, unique_id, name, device_info_extra=None):
        super().__init__(coordinator)
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._config_entry = config_entry
        self._device_info_extra = device_info_extra or {}

    @property
    def device_info(self) -> DeviceInfo:
        info = DeviceInfo(
            identifiers={(DOMAIN, self._config_entry.unique_id)},
            name=self._attr_name,
            manufacturer=MANUFACTURER,
            model="Tuya Thermostat",
            sw_version=None,
            configuration_url=None,
        )
        info.update(self._device_info_extra)
        return info

    @property
    def extra_state_attributes(self):
        return {
            ATTR_CARD_ROLE: getattr(self, "card_role", None),
            ATTR_CARD_TOKEN: getattr(self, "card_token", None),
        }
