from django import template

from app.settings import MEDIA_URL, STATIC_URL

register = template.Library()


@register.filter
def view_prop(value, arg):
    if value is not None:
        strresult = None
        try:
            strresult = getattr(value, arg)
        except:
            pass
        if strresult is not None:
            return strresult

    return ""


@register.filter
def get_bool_prop(value, arg):
    if value is not None:
        prop = getattr(value, arg)

        if prop is True:
            return "Activo"
        elif prop is False:
            return "Inactivo"

    return ""


@register.filter
def get_url_image(value, arg):
    if value is not None:
        strresult = None
        try:
            strresult = getattr(value, arg)
        except:
            pass
        if strresult:
            return '{}{}'.format(MEDIA_URL, strresult)
    return '{}{}'.format(STATIC_URL, 'img/user.png')


@register.filter
def get_type_user(value):
    if value is not None:
        if value.is_grocer:
            return 'bdg'
        elif value.is_laboratory_worker:
            return 'lab'
    return 'todo'
