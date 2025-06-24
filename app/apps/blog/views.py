from django.shortcuts import (
    render,
    get_object_or_404,
)
from .models import Category, Post


def index(request):
    template = "blog/index.html"

    posts = Post.objects.filter(is_published=True).order_by("-publish_date")
    categories = Category.objects.filter(is_active=True).order_by("name")

    context = {
        "posts": posts,
        "categories": categories,
    }

    return render(request, template, context)


def category_list(request):
    template = "blog/category-list.html"

    categories = Category.objects.filter(is_active=True).order_by("name")

    context = {
        "categories": categories,
    }

    return render(request, template, context)


def post_list(request):
    template = "blog/post-list.html"

    posts = Post.objects.filter(is_published=True).order_by("-publish_date")
    categories = Category.objects.filter(is_active=True).order_by("name")

    context = {
        "posts": posts,
        "categories": categories,
    }

    return render(request, template, context)


def category_detail(request, category_slug):
    template = "blog/category.html"

    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(
        category=category,
        is_published=True,
    ).order_by("-publish_date")

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, template, context)


def post_detail(request, post_slug):
    template = "blog/post.html"

    post = get_object_or_404(Post, slug=post_slug, is_published=True)
    categories = Category.objects.filter(is_active=True).order_by("name")

    context = {
        "post": post,
        "categories": categories,
    }

    return render(request, template, context)
