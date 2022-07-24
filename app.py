# Импортируем необходимые инструменты из модуля flask
from flask import Flask, render_template, send_from_directory, request

# Импортируем модуль functions для работы с форматом JSON
import functions

app = Flask(__name__)


# Создаём корневой маршрут
@app.route("/")
def main_page():
    """
    :return: Заполненный шаблон главной страницы
    """
    return render_template("index.html")


# Создаём маршрут для поиска постов по ключу
@app.route("/search")
def page_with_selected_posts():
    """
    :return: Заполненный шаблон всех постов с данным ключом
    """
    key_for_search = request.args.get("s")
    list_of_posts_for_output = []
    for i in functions.load_posts("posts.json"):
        if key_for_search.lower() in i["content"].lower():
            list_of_posts_for_output.append(i)
    return render_template("posts_list.html", _list=list_of_posts_for_output, key=key_for_search)


# Создаём маршрут для нового поста
@app.route("/post", methods=["GET"])
def page_post_form():
    """
    :return: Заполненный шаблон создания поста
    """
    return render_template("post_form.html")


@app.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    picture.save(f"./uploads/images/{picture.filename}")
    user_post = request.form.get("content")
    return render_template("post_uploaded.html", user_post=user_post)


# Создаём маршрут для каталога с пользовательскими загрузками
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
