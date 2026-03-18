"""
Constantes et mapping DP pour Tuya Thermostat
"""

# Data Points (DP) — confirmés par scan
DP_MODE = 101           # mode (écriture)
DP_CHILD_LOCK = 102     # verrou enfant
DP_VACATION_DURATION = 110  # durée vacances (jours)
DP_TEMP_SET = 125       # température cible (×10)
DP_TEMP_UNIT = 126      # unité (c/f)
DP_TEMP_CURRENT = 116   # température actuelle (×10)
DP_UPPER_TEMP = 129     # limite haute (×10)
DP_LOWER_TEMP = 130     # limite basse (×10)
DP_RUNNING_MODE = 131   # mode actif en lecture seule
DP_FAULT = 119          # alarme/défaut
DP_WINDOW_STATE = 123   # détection fenêtre ouverte
DP_BOOST_DURATION = 111
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

# Mapping label FR → valeur Tuya
MODES_MAP = {
    "Éteint":       "Standby",
    "Confort":      "Comfort",
    "Éco":          "ECO",
    "Hors-gel":     "Anti_forst",
    "Températures": "Thermostat",
    "Programmation":"Programming",
}
MODES_MAP_REVERSE = {v: k for k, v in MODES_MAP.items()}
MODES = list(MODES_MAP.keys())

# Unités
TEMP_UNIT_C = "c"
TEMP_UNIT_F = "f"

# Autres constantes
DOMAIN = "tuya_thermostat"
MANUFACTURER = "Tuya"

# Attributs custom pour la carte Lovelace
ATTR_CARD_ROLE = "tuya_thermostat_card_role"
ATTR_CARD_TOKEN = "tuya_thermostat_token"
