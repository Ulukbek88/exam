from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'author', 'email', 'text')
    list_display_links = ('pk', 'author')
    list_filter = ('author',)
    search_fields = ('author',)


admin.site.register(Review, ReviewAdmin)
