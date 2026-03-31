"""
Client tinytuya et dataclass ThermostatState
Ce module n'importe pas Home Assistant.
"""
import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Optional
import tinytuya

from .const import DP_MAP, MODES

@dataclass
class ThermostatState:
    temp_current: Optional[float] = None
    temp_set: Optional[float] = None
    mode: Optional[str] = None
    running_mode: Optional[str] = None
    child_lock: Optional[bool] = None
    fault: Optional[int] = None
    window_state: Optional[bool] = None
    temp_unit: Optional[str] = None
    upper_temp: Optional[float] = None
    lower_temp: Optional[float] = None
    boost_duration: Optional[int] = None
    vacation_duration: Optional[int] = None
    average_power: Optional[float] = None
    electricity_statistics: Optional[int] = None
    raw_dps: Optional[Dict[str, Any]] = None

class TuyaThermostatClient:
    def __init__(self, host: str, device_id: str, local_key: str, protocol_version: str = "3.3"):
        self._device = tinytuya.Device(device_id, host, local_key)
        self._device.set_version(protocol_version)
        self._lock = asyncio.Lock()

    async def async_status(self) -> ThermostatState:
        async with self._lock:
            loop = asyncio.get_running_loop()
            data = await loop.run_in_executor(None, self._device.status)
        dps = data.get("dps", {})
        state = ThermostatState(
            temp_current=self._parse_temp(dps.get(str(DP_MAP["temp_current"]))),
            temp_set=self._parse_temp(dps.get(str(DP_MAP["temp_set"]))),
            mode=dps.get(str(DP_MAP["mode"])),
            running_mode=dps.get(str(DP_MAP["running_mode"])),
            child_lock=dps.get(str(DP_MAP["child_lock"])),
            fault=dps.get(str(DP_MAP["fault"])),
            window_state=dps.get(str(DP_MAP["window_state"])),
            temp_unit=dps.get(str(DP_MAP["temp_unit"])),
            upper_temp=self._parse_temp(dps.get(str(DP_MAP["upper_temp"]))),
            lower_temp=self._parse_temp(dps.get(str(DP_MAP["lower_temp"]))),
            boost_duration=dps.get(str(DP_MAP["boost_duration"])),
            vacation_duration=dps.get(str(DP_MAP["vacation_duration"])),
            average_power=self._parse_power(dps.get(str(DP_MAP["average_power"]))),
            electricity_statistics=self._parse_energy(dps.get(str(DP_MAP["electricity_statistics"]))),
            raw_dps=dps,
        )
        return state

    async def async_set(self, dps: Dict[str, Any]) -> bool:
        async with self._lock:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(None, self._device.set_multiple_values, dps)
        return result.get("success", False)

    @staticmethod
    def _parse_temp(val: Any) -> Optional[float]:
        if val is None:
            return None
        try:
            return float(val) / 10.0
        except Exception:
            return None

    @staticmethod
    def _parse_power(val: Any) -> Optional[float]:
        if val is None:
            return None
        try:
            return float(val) / 10.0
        except Exception:
            return None

    @staticmethod
    def _parse_energy(val: Any) -> Optional[float]:
        if val is None:
            return None
        try:
            return float(val) / 10.0
        except Exception:
            return None
