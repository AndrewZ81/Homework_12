# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template, request

# Подключаем инструменты модуля functions
from functions import is_extension_allowed

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
    """
    :return: Заполненный шаблон созданного поста
    """
    picture = request.files.get("picture")
    if picture:
        file_name = picture.filename
        if is_extension_allowed(file_name):
            picture.save(f"./uploads/images/{picture.filename}")
            user_post = request.form.get("content")
            return render_template("post_uploaded.html", user_post=user_post, user_picture=picture.filename)
        else:
            return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
                   f"<p>Расширение выбранного файла недопустимо. " \
                   f"Вернитесь назад и попробуйте снова</p>" \
                   f"<a href='/post' class='button'>Назад</a></pre>"
    else:
        return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
               f"<p>Вы не загрузили файл. Вернитесь назад и попробуйте снова</p>" \
               f"<a href='/post' class='button'>Назад</a></pre>"
