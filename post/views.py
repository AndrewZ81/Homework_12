# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template, request

# Подключаем инструменты модуля functions для работы с форматом JSON
from functions import load_posts

# Создаём блюпринты страниц создания нового поста и созданного поста, соответственно
post_form_blueprint = Blueprint("post_form_blueprint", __name__, template_folder="templates")
post_uploaded_blueprint = Blueprint("post_uploaded_blueprint", __name__, template_folder="templates")


# Создаём эндпоинт страницы нового поста
@post_form_blueprint.route("/post", methods=["GET"])
def page_post_form():
    """
    :return: Заполненный шаблон создания поста
    """
    return render_template("post_form.html")


# Создаём эндпоинт страницы созданного поста
@post_uploaded_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    if picture:
        picture.save(f"./uploads/images/{picture.filename}")
        user_post = request.form.get("content")
        return render_template("post_uploaded.html", user_post=user_post, user_picture=picture.filename)
    else:
        return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
               f"<p>Вы не загрузили файл. Вернитесь назад и попробуйте снова</p>" \
               f"<a href='post' class='button'>Назад</a></pre>"
