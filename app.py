# Подключаем необходимые инструменты из модуля flask
from flask import Flask, send_from_directory

# Подключаем блюпринты
from index.views import index_blueprint
from search.views import search_blueprint
from post.views import post_form_blueprint, post_uploaded_blueprint

# Создаём наше приложение
app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(index_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(post_form_blueprint)
app.register_blueprint(post_uploaded_blueprint)

# Ограничиваем максимальный размер загружаемых файлов в 3 Mb
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024


# Создаём обработчик ошибки слишком большого размера загружаемого файла
@app.errorhandler(413)
def request_entity_too_large(error):
    """
    :param error:
    :return: Преформатированное описание слишком большого размера загружаемого файла
    """
    return f"<pre><link rel='stylesheet' href='/static/style.css'>" \
               f"<p>Размер загружаемого файла слишком велик. Вернитесь назад и попробуйте снова</p>" \
               f"<a href='post' class='button'>Назад</a></pre>", 413


# Создаём эндпоинт каталога с пользовательскими загрузками
@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    :param path: путь к файлу в каталоге загрузок пользователей
    :return: файл в каталоге загрузок пользователей
    """
    return send_from_directory("uploads", path)


app.run()
