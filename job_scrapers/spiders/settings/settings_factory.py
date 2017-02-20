from prospects_settings import ProspectsSettings
from reed_co_uk_settings import ReedCoUkSettings
from milkround_settings import MilkroundSettings


class SettingsFactory:
    @staticmethod
    def get_settings(name):
        if name == "prospects":
            return ProspectsSettings()
        elif name == "reed":
            return ReedCoUkSettings()
        elif name == "milkround":
            return MilkroundSettings()
        else:
            raise ValueError("Unknown settings name '%s'" % name)
