from datetime import date

from django.db.models import Count

from blog.models import Post


def q1():
    return Post.objects.filter(published=True)


def q2():
    return Post.objects.filter(category__isnull=True)


def q3():
    return Post.objects.filter(
        published=True,
        published_at__range=(date(2026, 3, 1), date(2026, 5, 31)),
    )


def q4():
    return Post.objects.annotate(n_comments=Count("comments")).filter(n_comments__gt=2)
