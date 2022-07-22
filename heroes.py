from abc import ABC, abstractmethod
from antagonistfinder import AntagonistFinder
from weapons import KickMixin, LazersMixin, RoundHouseKickMixin, GunMixin


class SuperHero(ABC):
    """ Создание Абстрактного класса SuperHero."""

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        """ Поиск врагов по месту.
        Аргументы:
        place - дочерний класс Place
        """
        self.finder.get_antagonist_in_place(place)

    @abstractmethod
    def attack(self):
        """ Простая атака героя."""
        pass

    @abstractmethod
    def ultimate(self):
        """ Окончательная атака героя."""
        pass


class Superman(SuperHero, KickMixin, LazersMixin):
    """ Создание дочернего класса от SuperHero, с классами-миксинами KickMixin, LazersMixin."""

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def attack(self):
        self.kick()

    def ultimate(self):
        self.incinerate_with_lasers()


class ChuckNorris(SuperHero, RoundHouseKickMixin, GunMixin):
    """ Создание дочернего класса от  SuperHero, с классами-миксинами RoundHouseKickMixin, GunMixin."""

    def __init__(self):
        super(ChuckNorris, self).__init__('Chuck Norris', False)

    def attack(self):
        self.roundhouse_kick()

    def ultimate(self):
        self.fire_a_gun()
