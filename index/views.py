# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template

# Создаём блюпринт главной страницы
index_blueprint = Blueprint("index_blueprint", __name__, template_folder="templates")


@index_blueprint.route("/")
def main_page():
    """
    Создаёт эндпоинт для главной страницы
    :return: Заполненный шаблон главной страницы
    """
    return render_template("index.html")
