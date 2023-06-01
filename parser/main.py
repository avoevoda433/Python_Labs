from findActor import find_actor
from selenium import webdriver
from fake_useragent import UserAgent
from getFilms import get_common_films


user_agent = UserAgent()

# START WEBDRIVER
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={user_agent.random}")
options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path=r"C:\Users\avoev\Универ\findFilms-parser\webdriver\chromedriver.exe",
    options=options
)


def input_actor_info():
    first_actor = input("First actor name: ")
    second_actor = input("Second actor name: ")
    link1 = find_actor(driver, first_actor)
    link2 = find_actor(driver, second_actor)
    if not link1 or not link2:
        print("Сheck actors name and try again")
        input_actor_info()
    else:
        return [link1[0]["link"].split("/")[4], link2[0]["link"].split("/")[4]]


if __name__ == "__main__":
    films = get_common_films(driver, input_actor_info())
    print(films if films else "No shared movies found")

#driver.close()
#driver.quit()