# Подключаем для создания блюпринтов на основе шаблонов
import logging

from flask import Blueprint, render_template, request

# Подключаем инструменты логирования
import logging

# Подключаем инструменты модуля functions для работы с форматом JSON
from functions import load_posts

# Настраиваем логирование
searching_logger = logging.getLogger(__name__)  # для логирования поиска постов
searching_logger.setLevel(logging.INFO)
searching_handler = logging.FileHandler("search_log.txt", encoding="utf-8")
searching_formatter = logging.Formatter("%(asctime)s : %(message)s")
searching_handler.setFormatter(searching_formatter)
searching_logger.addHandler(searching_handler)


# Создаём блюпринт страницы поиска по постам
search_blueprint = Blueprint("search_blueprint", __name__, template_folder="templates")


# Создаём эндпоинт страницы поиска по постам ключём
@search_blueprint.route("/search")
def page_with_selected_posts():
    """
    :return: Заполненный шаблон всех постов с данным ключом
    """
    key_for_search = request.args.get("s")
    if not key_for_search:
        searching_logger.info("Не введен текст для поиска")
        return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
                f"<p>Вы не ввели текст для поиска. " \
                f"Вернитесь назад и попробуйте снова</p>" \
                f"<a href='/' class='button'>Назад</a></pre>"
    else:
        searching_logger.info(f"Выполнен поиск {key_for_search}")
        list_of_posts_for_output = []
        for i in load_posts("posts.json"):
            if key_for_search.lower() in i["content"].lower():
                list_of_posts_for_output.append(i)
        return render_template("posts_list.html", _list=list_of_posts_for_output, key=key_for_search)
