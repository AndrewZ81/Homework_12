# Подключаем для создания блюпринтов на основе шаблонов
from flask import Blueprint, render_template, request

# Подключаем инструменты модуля functions
from functions import is_extension_allowed, save_post

# Подключаем инструменты логирования
import logging

# Создаём блюпринты страниц создания нового поста и созданного поста, соответственно
post_form_blueprint = Blueprint("post_form_blueprint", __name__, template_folder="templates")
post_uploaded_blueprint = Blueprint("post_uploaded_blueprint", __name__, template_folder="templates")

# Настраиваем логирование
extension_checker_logger = logging.getLogger(__name__)
extension_checker_logger.setLevel(logging.INFO)
extension_checker_handler = logging.FileHandler("ext_check_log.txt", encoding="utf-8")
extension_checker_formatter = logging.Formatter("%(asctime)s : %(message)s")
extension_checker_handler.setFormatter(extension_checker_formatter)
extension_checker_logger.addHandler(extension_checker_handler)


@post_form_blueprint.route("/post", methods=["GET"])
def page_post_form():
    """
    Создаёт эндпоинт страницы нового поста
    :return: Заполненный шаблон создания поста
    """
    return render_template("post_form.html")


@post_uploaded_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    """
    Создаёт эндпоинт страницы загруженного поста
    :return: Заполненный шаблон загруженного поста
    """
    picture = request.files.get("picture")
    if picture:
        file_name = picture.filename
        if is_extension_allowed(file_name):
            extension_checker_logger.info(f"Загружен файл {picture.filename}")
            picture.save(f"./uploads/images/{picture.filename}")
            user_post = request.form.get("content")
            save_post("posts.json", {'pic': f"./uploads/images/{picture.filename}", 'content': f"{user_post}"})
            return render_template("post_uploaded.html", user_post=user_post, user_picture=picture.filename)
        else:
            extension_checker_logger.info(f"Расширение выбранного файла {picture.filename} недопустимо")
            return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
                   f"<p>Расширение выбранного файла недопустимо. " \
                   f"Вернитесь назад и попробуйте снова</p>" \
                   f"<a href='/post' class='button'>Назад</a></pre>"
    else:
        return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
               f"<p>Вы не загрузили файл. Вернитесь назад и попробуйте снова</p>" \
               f"<a href='/post' class='button'>Назад</a></pre>"
