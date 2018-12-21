from django import template

register = template.Library()


@register.filter(name='unique_cities')
def unique_cities(obj):
    return obj.get_unique_cities()
