from methods.UiRequests import UiRequest
from selenium import webdriver
import pytest
import allure


@allure.epic("UI-tests")
@pytest.fixture
def driver() -> UiRequest:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(4)
    request = UiRequest(browser)
    yield request
    browser.quit()


@allure.id("UI-1")
@allure.title("Поиск фильма по подборкам")
def test_search_in_lists(driver: UiRequest):
    with allure.step("Заполнение поля ссылкой на список, номер фильма в списке и его название"):
        list = "/top250/"
        number_in_list = 0
        title = "1+1"
    with allure.step("Запрос фильма из списка, сравниваем название"):
        text = driver.get_title_from_collection(list, number_in_list)
    assert text == title


@allure.id("UI-2")
@allure.title("Использование функции расширенного поиска по стране и жанру")
def test_search_mechanism(driver: UiRequest):
    with allure.step("Заполнение поля страна и жанр"):
        country = "Корея Южная"
        genre = "ужасы"
    with allure.step("Поиск по конкретным параметрам"):
        result = driver.search_by_country_and_genre(country, genre)
    assert "Результаты поиска" in result


@allure.id("UI-3")
@allure.title("Поиск конкретного фильма и актёра в главной роли")
def test_search_for_film(driver: UiRequest):
    with allure.step("Выбор интересующего фильма и указание имени актёра"):
        title = "Драйв"
        actor = "Райан Гослинг"
    with allure.step("Запрос на поиск фильма по названию"):
        driver.searching_for_film(title)
    with allure.step("Выбор первого фильма из поисковой выдачи"):
        driver.search_film_results()
    with allure.step("Проверка актёра в главной роли"):
        result = driver.find_main_cast()
    assert actor in result


@allure.id("UI-4")
@allure.title("Поиск фильма из списка лучших у актёра")
def test_actor_film_list(driver: UiRequest):
    with allure.step("Выбор интересующего актёра и указание фильма, в котором он играл"):
        name = "Вин Дизель"
        title = "Форсаж"
    with allure.step("Запрос на поиск актёра по имени"):
        driver.searching_for_film(name)
    with allure.step("Получение первого актёра из списка, переход на страницу"):
        driver.search_person_results()
    with allure.step("Получение списка лучших фильмов актёра"):
        films = driver.get_top_films_by_actor()
    assert title in films


@allure.id("UI-5")
@allure.title("Поиск фильма по режиссёру")
def test_director_film_list(driver: UiRequest):
    with allure.step("Выбор интересующего режиссёра и указание фильма, который он снимал"):
        name = "Кристофер Нолан"
        title = "Оппенгеймер"
    with allure.step("Запрос на поиск режиссёра по имени"):
        driver.searching_for_film(name)
    with allure.step("Получение первого персонажа, переход на страницу"):   
        driver.search_person_results()
    with allure.step("Получение списка всех фильмов режиссёра"):
        films = driver.get_film_list_of_director()
    assert title in films
