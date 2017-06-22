from django import template
from first_a.models import First_a
register = template.Library()


@register.filter(name='times')
def times(number):
    return range(1, number)

@register.filter(name='students')
def students(number):
    return First_a


