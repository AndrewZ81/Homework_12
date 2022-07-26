# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template, request

# Подключаем инструменты модуля functions для работы с форматом JSON
from functions import load_posts

# Создаём блюпринт страницы поиска по постам
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


# Создаём эндпоинт страницы поиска по постам ключём
@search_blueprint.route("/search")
def page_with_selected_posts():
    """
    :return: Заполненный шаблон всех постов с данным ключом
    """
    key_for_search = request.args.get("s")
    list_of_posts_for_output = []
    for i in load_posts("posts.json"):
        if key_for_search.lower() in i["content"].lower():
            list_of_posts_for_output.append(i)
    return render_template("posts_list.html", _list=list_of_posts_for_output, key=key_for_search)
