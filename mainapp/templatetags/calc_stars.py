from django import template

register = template.Library()

@register.filter(name='stars')
def stars(value):
    return round(value * 2) / 2
