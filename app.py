# Импортируем необходимые инструменты из модуля flask
from flask import Flask, render_template, send_from_directory

# Импортируем модуль functions для работы с форматом JSON
import functions

app = Flask(__name__)

@app.route("/")
def main_page():
    """
    :return: Заполненный шаблон главной страницы
    """
    return render_template("index.html")


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
