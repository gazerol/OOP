from abc import ABC, abstractmethod


class Place(ABC):
    """ Создание Абстрактного класса Place."""

    @abstractmethod
    def get_antagonist(self):
        """ Поиск врага по месту."""
        pass


class Kostroma(Place):
    """ Создание дочернего класса от Place."""
    name = 'Kostroma'

    def get_antagonist(self):
        print('Orcs hid in the forest')


class Tokyo(Place):
    """ Создание дочернего класса от Place."""
    name = 'Tokyo'

    def get_antagonist(self):
        print('Godzilla stands near a skyscraper')


class Planet(Place):
    """ Создание дочернего класса от Place."""
    coordinates = [3.13243, 4.314355]

    def get_antagonist(self):
        print('Aliens were hiding in the space station')
