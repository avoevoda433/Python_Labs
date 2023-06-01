from getActorFilms import get_actor_films


def intersection_list(list1, list2):
    ready_list = []
    for item in list1:
        if (item["name"] in [i["name"] for i in list2]) and item["year"] in [i["year"] for i in list2]:
            ready_list.append(item)
    return ready_list


def get_common_films(driver, list_actors):
    common_films = []
    try:
        if list_actors:
            list_actors_films = []

            for link_actor in list_actors:
                list_actors_films.append(list(get_actor_films(driver, link_actor)))

            if len(list_actors_films) > 1:
                common_films = list(list_actors_films[0])

                for index in range(1, len(list_actors_films)):
                    common_films = intersection_list(common_films, list_actors_films[index])
            else:
                common_films = list_actors_films[0]

    except Exception as ex:
        error_msg = ex

    finally:
        return common_films
