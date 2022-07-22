class KickMixin:
    """ Создание класса-миксина для удара."""

    @staticmethod
    def kick():
        print('Kick')


class LazersMixin:
    """ Создание класса-миксина для лазеров."""

    @staticmethod
    def incinerate_with_lasers():
        print('Wzzzuuuup!')


class RoundHouseKickMixin:
    """ Создание класса-миксина для удара с разворота."""

    @staticmethod
    def roundhouse_kick():
        print('Bump')


class GunMixin:
    """ Создание класса-миксина для выстрела выстрела и оружия."""

    @staticmethod
    def fire_a_gun():
        print('PIU PIU')
