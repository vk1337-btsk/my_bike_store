from django.contrib import admin

from journal.models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'flag_publication', 'count_views',)
    list_filter = ('title',)
    search_fields = ('title',)

