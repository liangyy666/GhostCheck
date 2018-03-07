# coding:utf-8

from django.contrib import admin
from . import models

class GhostAdmin(admin.ModelAdmin):
    list_display = ('name', 'chapter_name')

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('chapter_name', 'ghost_name', 'fight_ghost')

admin.site.register(models.Chapter, ChapterAdmin)
# admin.site.register(models.Ghost, GhostAdmin)
