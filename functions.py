# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


def load_posts(file_with_posts):
    """
    Загружает посты
    :param file_with_posts: Файл для загрузки с постами формата JSON
    :return: Список постов
    """
    try:
        file = open(file_with_posts, encoding="utf-8")
        posts = json.load(file)
    except FileNotFoundError:
        quit(f"Файл {file_with_posts} с постами для загрузки не найден")
    except JSONDecodeError:
        quit(f"Файл {file_with_posts} с постами для загрузки не удалось считать")
    else:
        file.close()
        return posts


def save_post(file_with_posts, uploaded_post):
    """
    Сохраняет загруженный пост
    :param file_with_posts: Файл для сохранения с постами формата JSON
    :param uploaded_post: Загруженный пост в формате словаря
    :return: Сохраненный файл с постами формата JSON
    """
    posts = load_posts(file_with_posts)
    posts.append(uploaded_post)
    file = open(file_with_posts, "w", encoding="utf-8")
    return json.dump(posts, file, indent=2, ensure_ascii=False)


def is_extension_allowed(file_name):
    """
    Проверяет расширение файла
    :param file_name: Полное имя загружаемого файла при создании поста
    :return: Логическое значение по результату проверки допустимости расширения файла
    """
    allowed_extensions = {"jpg", "jpeg", "bmp", "png"}
    extension = file_name.split(".")[-1]
    if extension in allowed_extensions:
        return True
    else:
        return False
