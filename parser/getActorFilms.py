from selenium.webdriver.common.by import By
import time


def get_actor_films(driver, actor_link):
    films = []
    actors = []
    url = f"https://www.imdb.com/name/{actor_link}"

    try:
        driver.get(url=url)
        driver.maximize_window()
        driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior = "auto"')
        accordion_expander = driver.find_element(By.XPATH, "//button[@data-testid='nm-flmg-all-accordion-expander']")
        accordion_expander.click()

        time.sleep(3)

        accordion_item_films = driver.find_elements(By.XPATH,
                                                    "//label[@for='accordion-item-actor-previous-projects']/.."
                                                    "//following-sibling::div[@class='ipc-accordion__item__content']"
                                                    "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                    "//div[@class='ipc-metadata-list-summary-item__c'] | "
                                                    "//label[@for='accordion-item-actress-previous-projects']/.."
                                                    "//following-sibling::div[@class='ipc-accordion__item__content']"
                                                    "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                    "//div[@class='ipc-metadata-list-summary-item__c']")
        accordion_item_films_link = driver.find_elements(By.XPATH,
                                                         "//label[@for='accordion-item-actor-previous-projects']/..//"
                                                         "following-sibling::div[@class='ipc-accordion__item__content']"
                                                         "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                         "//div[@class='ipc-metadata-list-summary-item__c']"
                                                         "//a[@class='ipc-metadata-list-summary-item__t'] | "
                                                         "//label[@for='accordion-item-actress-previous-projects']/..//"
                                                         "following-sibling::div[@class='ipc-accordion__item__content']"
                                                         "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                         "//div[@class='ipc-metadata-list-summary-item__c']"
                                                         "//a[@class='ipc-metadata-list-summary-item__t']")
        accordion_item_films_img = driver.find_elements(By.XPATH,
                                                        "//label[@for='accordion-item-actor-previous-projects']/..//"
                                                        "following-sibling::div[@class='ipc-accordion__item__content']"
                                                        "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                        "//*[@class='ipc-image' or @class='ipc-icon ipc-icon--movie "
                                                        "ipc-icon--inline ipc-media__icon'] | "
                                                        "//label[@for='accordion-item-actress-previous-projects']/..//"
                                                        "following-sibling::div[@class='ipc-accordion__item__content']"
                                                        "//li[contains(@class,'ipc-metadata-list-summary-item')]"
                                                        "//*[@class='ipc-image' or @class='ipc-icon ipc-icon--movie "
                                                        "ipc-icon--inline ipc-media__icon']")

        if len(accordion_item_films) > 0:
            for film_id in range(len(accordion_item_films)):
                films.append({
                    "name": accordion_item_films[film_id].text.split("\n")[0],
                    "year": accordion_item_films[film_id].text.split("\n")[2],
                    "link": accordion_item_films_link[film_id].get_attribute("href"),
                    "img": "https://media.istockphoto.com/id/944677678/vector/"
                           "movie-camera-icon.jpg?s=170667a&w=0&k=20&c=Q8-bm3GnwhD1FBsXLdmxPyI4wf_umUWxlgM6c9u5AQA="
                    if not (str(accordion_item_films_img[film_id].tag_name) == "img")
                    else accordion_item_films_img[film_id].get_attribute("src")
                })

    except Exception as ex:
        error_msg = ex

    finally:
        return films
