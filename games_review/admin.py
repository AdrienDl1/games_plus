from django.contrib import admin
from games_review.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', )
    search_fields = ('name', )
    list_filter = ('types', )
# Register your models here.

admin.site.register(Type)
admin.site.register(Game, GameAdmin)