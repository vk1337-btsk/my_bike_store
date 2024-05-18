from django import template

register = template.Library()


@register.filter
def check_group(user):
    return user.groups.filter(name='Moderator').exists()
