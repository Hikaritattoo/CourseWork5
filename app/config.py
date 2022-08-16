import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class BaseConfig:
    EQUIPMENT_PATH = os.path.join(os.path.dirname(BASE_DIR), 'data/equipment.json')
    STAMINA_RECOVERY_PER_TURN = 1
    DEBUG = True
    LOG_FILE = os.path.join(os.path.dirname(BASE_DIR), 'data/log.log')

