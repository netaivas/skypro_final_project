from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class UiRequest:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__driver.get("https://www.kinopoisk.ru/lists/categories/movies/1/")

    def get_title_from_collection(self, collection: str, num: int):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"a[href='/lists/movies{collection}']")))
        self.__driver.find_element(By.CSS_SELECTOR, f"a[href='/lists/movies{collection}']").click()
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.styles_title__jB8AZ")))
        title = self.__driver.find_elements(By.CSS_SELECTOR, "span[data-tid='4502216a']")
        return title[num].text

    def search_by_country_and_genre(self, country: str, genre: str):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/s/']")))
        self.__driver.find_element(By.CSS_SELECTOR, "a[href='/s/']").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#searchAdv")))
        select_country = self.__driver.find_element(By.CSS_SELECTOR, "select#country")
        select = Select(select_country)
        select.select_by_visible_text(country)
        select_genre = self.__driver.find_element(By.CSS_SELECTOR, "select.text.el_6.__genreSB__")
        select = Select(select_genre)
        select.select_by_visible_text(genre)
        self.__driver.find_element(By.CSS_SELECTOR, "#formSearchMain > input.el_18.submit.nice_button").click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.search_results")))
        results = self.__driver.find_element(By.CSS_SELECTOR, "div.search_results.search_results_last")
        return results.text

    def searching_for_film(self, title: str):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/s/']")))
        self.__driver.find_element(By.CSS_SELECTOR, "input[name=kp_query]").click()
        self.__driver.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys(title, Keys.RETURN)

    def search_film_results(self):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.element.most_wanted")))
        mw = self.__driver.find_element(By.CSS_SELECTOR, "div.element.most_wanted")
        mw.find_element(By.CSS_SELECTOR, "a[data-type='film']").click()

    def find_main_cast(self):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dub.dub1.dub_first")))
        actor = self.__driver.find_element(By.CSS_SELECTOR, "div.dub.dub1.dub_first")
        actor_name = actor.find_element(By.CSS_SELECTOR, "div.name")
        return actor_name.text

    def search_person_results(self):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.element.most_wanted")))
        mw = self.__driver.find_element(By.CSS_SELECTOR, "div.element.most_wanted")
        name = mw.find_element(By.CSS_SELECTOR, "p.name")
        name.find_element(By.CSS_SELECTOR, "a[data-type='person']").click()

    def get_top_films_by_actor(self):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.styles_bestMovies__P4zSv")))
        film_list = self.__driver.find_elements(By.CSS_SELECTOR, "a.styles_link__Act80")
        list_of_films = [film.text for film in film_list]
        return list_of_films

    def get_film_list_of_director(self):
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.styles_bestMovies__P4zSv")))
        self.__driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        film_list = self.__driver.find_elements(By.CSS_SELECTOR, "span[data-tid='4502216a']")
        list_of_films = [film.text for film in film_list]
        return list_of_films
