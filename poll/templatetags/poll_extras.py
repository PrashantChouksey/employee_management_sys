from django import template
from poll.models import Qus

register= template.Library()

def upper(value):
    """Converts string in UPPER case"""
    return value.upper()

register .filter('upper', upper)


@register.simple_tag
def recent_polls(n=5, **kwargs):
    qus = Qus.objects.all().order_by('-created_at')
    return qus[0:n]
