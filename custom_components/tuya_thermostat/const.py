"""
Constantes et mapping DP pour Tuya Thermostat
"""

# Data Points (DP) — confirmés par scan
DP_MODE = 101               # mode (écriture) : Standby/Comfort/ECO/Anti_forst/Thermostat/Programming
DP_CHILD_LOCK = 102         # verrou enfant (bool)
DP_VACATION_DURATION = 110  # durée vacances (jours, entier)
DP_BOOST_DURATION = 111     # durée boost (minutes, entier)
DP_ELEC_STATS = 112         # statistiques électriques cumulées (unité inconnue)
DP_TEMP_CURRENT = 116       # température actuelle (×10, °C)
DP_AVERAGE_POWER = 117      # puissance moyenne sur delta t (×10, W) — NON instantanée
DP_TEMP_CORRECTION = 118    # correction/calibration température (×10, °C)
DP_FAULT = 119              # alarme/défaut (bitmask entier)
DP_WINDOW_OPEN = 122        # détection fenêtre activée (bool)
DP_WINDOW_STATE = 123       # fenêtre ouverte détectée (bool, lecture seule)
DP_WINDOW_DURATION = 124    # durée avant détection fenêtre (minutes)
DP_TEMP_SET = 125           # température cible (×10, °C)
DP_TEMP_UNIT = 126          # unité température (c/f)
DP_HYSTERESIS = 128         # hystérésis (×10, °C)
DP_UPPER_TEMP = 129         # limite haute température (×10, °C)
DP_LOWER_TEMP = 130         # limite basse température (×10, °C)
DP_RUNNING_MODE = 131       # mode actif (lecture seule)

# DPs non identifiés
# DP 121 = 31  : inconnu (valeur fixe)
# DP 127 = 2   : type de programmation ? (7 jours)

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
