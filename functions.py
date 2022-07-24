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
