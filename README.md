# Tuya Thermostat (LAN) pour Home Assistant

Intégration custom Home Assistant pour thermostat Tuya en communication locale (LAN), compatible HACS.

## Installation

1. Copier le dossier `custom_components/tuya_thermostat` dans votre dossier Home Assistant.
2. Redémarrer Home Assistant.
3. Ajouter l'intégration via l'UI.

## Fonctionnalités
- Contrôle local (LAN) sans cloud
- Support multi-appareils
- Plateformes : climate, sensor, binary_sensor, switch, number, select
- Polling configurable
- Diagnostics complets
- Carte Lovelace custom (à venir)

## Dépendances
- Python 3.11+
- [tinytuya](https://github.com/jasonacox/tinytuya) >= 1.16.0

## Développement

Structure inspirée du projet [EV Charger Tuya](https://github.com/lachand/EV_charger).

## Licence
MIT
