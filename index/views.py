# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template

# Создаём блюпринт главной страницы
index_blueprint = Blueprint("index_blueprint", __name__, template_folder="templates")


# Создаём эндпоинт для главной страницы
@index_blueprint.route("/")
def main_page():
    """
    :return: Заполненный шаблон главной страницы
    """
    return render_template("index.html")
