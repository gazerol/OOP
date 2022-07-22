from typing import Union
from heroes import Superman, SuperHero, ChuckNorris
from places import Kostroma, Tokyo, Planet
from MassMedia import Tv, Newspaper, Media


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo, Planet], media: Media):
    """ Старт сражения.
    Аргументы:
    hero - герой, защищающий территорию
    place - место сражения
    media - новостной канал информирования через Newspaper или Tv
    """
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    media.create_news(hero, place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma(), Newspaper())
    print('-' * 20)
    save_the_place(ChuckNorris(), Tokyo(), Tv())
    print('-' * 20)
    save_the_place(Superman(), Planet(), Newspaper())
