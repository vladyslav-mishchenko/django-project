from django.shortcuts import (
    render,
    get_object_or_404,
)
from .models import Page


def home(request):
    slug = "home"
    template = "pages/home.html"

    page = get_object_or_404(Page, slug=slug, is_published=True)

    context = {
        "page": page,
    }

    return render(request, template, context)


def about(request):
    slug = "about"
    template = "pages/about.html"

    page = get_object_or_404(Page, slug=slug, is_published=True)

    context = {
        "page": page,
    }

    return render(request, template, context)


def contacts(request):
    slug = "contacts"
    template = "pages/contacts.html"

    page = get_object_or_404(Page, slug=slug, is_published=True)

    context = {
        "page": page,
    }

    return render(request, template, context)
