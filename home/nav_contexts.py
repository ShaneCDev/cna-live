from products.models import Category


def categories_nav(request):
    categories = list(Category.objects.all())
    return {'categories': categories}