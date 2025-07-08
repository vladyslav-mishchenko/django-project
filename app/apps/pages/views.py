from django.shortcuts import (
    render,
    get_object_or_404,
)
from .models import Page


def page_detail(request, page_slug):

    page = get_object_or_404(Page, slug=page_slug, is_published=True)
    template = f"pages/{page.template}.html"

    context = {
        "page": page,
    }

    return render(request, template, context)
