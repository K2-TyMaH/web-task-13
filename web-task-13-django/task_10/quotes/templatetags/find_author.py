from django import template

from ..models import Author

register = template.Library()


def get_author(id_):
    author = Author.objects.get(id=id_)
    return author

register.filter('author', get_author)
