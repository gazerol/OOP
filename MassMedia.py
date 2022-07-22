from abc import ABC, abstractmethod


class PlaceName:

    @staticmethod
    def get_place_name(place):
        place_name = getattr(place, 'name', 'place')
        if hasattr(place, 'coordinates'):
            place_name = getattr(place, 'coordinates', 'place')
        return place_name


class Media(ABC):
    """ Создание Абстрактного класса Media."""

    @abstractmethod
    def create_news(self, hero, place):
        """ Выводит новость посредством Newspaper или Tv."""
        pass


class Newspaper(Media):
    """ Создание дочернего класса от Media."""

    def create_news(self, hero, place):
        place_name = PlaceName.get_place_name(place)
        print(f'{hero.name} saved the {place_name}! -- News from the newspaper')


class Tv(Media):
    """ Создание дочернего класса от Media."""

    def create_news(self, hero, place):
        place_name = PlaceName.get_place_name(place)
        print(f'{hero.name} saved the {place_name}! -- News from TV')
