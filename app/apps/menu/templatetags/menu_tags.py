from django import template
from apps.menu.models import Menu

register = template.Library()


# TODO: Refactor this to use soon for clarity
# instead of manual registration for better readability and standardization.
# @register.inclusion_tag("menu/main-menu.html", takes_context=True)
def render_menu(context, slug):
    try:
        menu = Menu.objects.get(slug=slug)
        items = menu.items.all()
    except Menu.DoesNotExist:
        items = []

    return {
        "menu_items": items,
        "menu_slug": slug,
        "request": context.get("request"),
    }


# TODO: remove when start to use decorator
register.inclusion_tag("menu/main-menu.html", takes_context=True)(render_menu)
