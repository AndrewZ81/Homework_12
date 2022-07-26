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


# Создаём эндпоинт каталога с пользовательскими загрузками
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
