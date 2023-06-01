from selenium.webdriver.common.by import By


def find_actor(driver, actor_name):
    actors = [] 
    url = f"https://www.imdb.com/find/?q={'%20'.join(actor_name.split())}&s=nm&ref_=fn_nm_pop"
    
    try:
        driver.get(url=url)
        driver.maximize_window()
        actors_a = driver.find_elements(By.CSS_SELECTOR,
                                        "section[data-testid='find-results-section-name'] "
                                        "a.ipc-metadata-list-summary-item__t")
        num_of_actors = len(actors_a)
        for actor_id in range(1, 4 if (num_of_actors >= 4) else num_of_actors):
            actors.append({
                "id": actor_id,
                "link": actors_a[actor_id-1].get_attribute("href"),
                "name": actors_a[actor_id-1].text
            })

    except Exception:
        actors = []

    finally:
        return actors


