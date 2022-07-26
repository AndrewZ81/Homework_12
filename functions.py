# Импортируем модуль JSON для работы с этим форматом
import json
from json import JSONDecodeError


def load_posts(file_with_posts):
    """
    :param file_with_posts: Файл с постами формата JSON
    :return: Список постов
    """
    try:
        file = open(file_with_posts, encoding="utf-8")
        posts = json.loads(file.read())
    except FileNotFoundError:
        quit("Файл с постами не найден")
    except JSONDecodeError:
        quit("Файл с постами не удалось считать")
    else:
        file.close()
        return posts


def is_extension_allowed(file_name):
    """
    :param file_name: Полное имя загружаемого файла при создании поста
    :return: Логическое значение по результату проверки допустимости расширения файла
    """
    allowed_extensions = {"jpg", "jpeg", "bmp", "png"}
    extension = file_name.split(".")[-1]
    if extension in allowed_extensions:
        return True
    else:
        return False
