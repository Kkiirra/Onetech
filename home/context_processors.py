from .models import Category


def categories(request):
    return {
        'categories': Category.objects.order_by('name')
    }


def favorites(request):
    if request.user.is_authenticated:
        return {
            'favorites': len(request.user.favorites.all())
        }
    else:
        return {
            'favorites': 0
        }
