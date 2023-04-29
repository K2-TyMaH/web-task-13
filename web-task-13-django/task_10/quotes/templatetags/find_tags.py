from django import template

from ..models import Tag, Quote

register = template.Library()


def get_tags(id_):
    quote = Quote.objects.get(id=id_)
    q_tags = quote.tags.all()
    return list(q_tags)


register.filter('tags', get_tags)
