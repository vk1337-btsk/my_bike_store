from django.contrib import admin

from apps.journal.models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'flag_publication', 'count_views', 'image', 'owner')
    list_filter = ('title',)
    search_fields = ('title',)
