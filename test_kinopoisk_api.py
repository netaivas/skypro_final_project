from methods.ApiTest import ApiTest
import allure


api = ApiTest("https://kinopoiskapiunofficial.tech")

@allure.epic("API-tests")
@allure.id("API-1")
@allure.title("Поиск фильма по ID на сервисе")
def test_get_film_by_id():
    with allure.step("Указать id интересующего фильма и его название на сервисе"):
        id = 435
        title_name = "Зеленая миля"
    with allure.step("Получение информации о фильме по ID"):
        result = api.get_film_by_id(id)
    assert result["nameRu"] == title_name


@allure.id("API-2")
@allure.title("Получение списка фильмов по подоборке")
def test_get_collection_films():
    with allure.step("Указать подборку фильмов или сериалов сервиса"):
        collection = "LOVE_THEME"
    with allure.step("Получение списка контента из подборки"):
        result = api.get_collection_list(collection)
    assert result["total"] > 0


@allure.id("API-3")
@allure.title("Поиск списка контента по рейтингу и годам выпуска")
def test_get_film_by_params():
    with allure.step("Передача года выхода контента, рейтинга и порядка отображения"):
        order = "RATING"
        type_of = "FILM"
        rating_from = "7"
        rating_to = "10"
        year_from = "2001"
        year_to = "2001"
    with allure.step("Указание конкретного фильма для поиска в списке"):
        top_rated = "Властелин колец: Братство Кольца"
    with allure.step("Получение списка по заданным параметрам"):
        result = api.get_list_of_content_by_params(order, type_of, rating_from, rating_to, year_from, year_to)
    assert result["items"][0]["nameRu"] == top_rated


@allure.id("API-4")
@allure.title("Поиск актёра по ID фильма")
def test_get_staff_by_film_id():
    with allure.step("Передача ID фильма и имени актёра, который в нём играл"):
        film_id = 276598
        actor_name = "Райан Гослинг"
    with allure.step("Поиск информации о лицах"):
        result = api.get_staff_by_film_id(film_id)
    assert result[1]["nameRu"] == actor_name


@allure.id("API-5")
@allure.title("Получение списка фильмов по ID актёра")
def test_get_film_list_by_actor():
    with allure.step("Передача ID актёра и названия фильма, в котором он играл"):
        actor_id = 11437
        film_title = "Форсаж"
    with allure.step("Получение информации об актёре"):
        result = api.get_actor_info(actor_id)
    assert any(film["nameRu"] == film_title for film in result["films"])