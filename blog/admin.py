from django.contrib import admin
from .models import Blog, Quote


class QuoteAdmin(admin.StackedInline):
    model = Quote
    max_num = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [QuoteAdmin]

    list_display = ['title', 'head', ]
    prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Blog
