"""
Constantes et mapping DP pour Tuya Thermostat
"""

# Data Points (DP) principaux
DP_MODE = 101
DP_CHILD_LOCK = 102
DP_TEMP_CURRENT = 116
DP_TEMP_SET = 125
DP_RUNNING_MODE = 131
DP_FAULT = 119
DP_WINDOW_STATE = 123
DP_TEMP_UNIT = 126
DP_UPPER_TEMP = 129
DP_LOWER_TEMP = 130
DP_BOOST_DURATION = 111
DP_VACATION_DURATION = 110
DP_AVERAGE_POWER = 117
DP_ELEC_STATS = 112

# Mappings pour HA
DP_MAP = {
    "mode": DP_MODE,
    "child_lock": DP_CHILD_LOCK,
    "temp_current": DP_TEMP_CURRENT,
    "temp_set": DP_TEMP_SET,
    "running_mode": DP_RUNNING_MODE,
    "fault": DP_FAULT,
    "window_state": DP_WINDOW_STATE,
    "temp_unit": DP_TEMP_UNIT,
    "upper_temp": DP_UPPER_TEMP,
    "lower_temp": DP_LOWER_TEMP,
    "boost_duration": DP_BOOST_DURATION,
    "vacation_duration": DP_VACATION_DURATION,
    "average_power": DP_AVERAGE_POWER,
    "electricity_statistics": DP_ELEC_STATS,
}

# Modes supportés (à compléter dynamiquement si besoin)
MODES = [
    "off", "heat", "cool", "auto", "fan", "standby"
]

# Unités
TEMP_UNIT_C = "c"
TEMP_UNIT_F = "f"

# Autres constantes
DOMAIN = "tuya_thermostat"
MANUFACTURER = "Tuya"

# Attributs custom pour la carte Lovelace
ATTR_CARD_ROLE = "tuya_thermostat_card_role"
ATTR_CARD_TOKEN = "tuya_thermostat_token"
