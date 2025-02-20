import random

from django import template

register = template.Library()


@register.filter(name='random')
def randomize(queryset):
    return sorted(queryset, key=lambda x: random.random())
