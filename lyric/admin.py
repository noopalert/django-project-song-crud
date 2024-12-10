from django.contrib import admin
from .models import Lyric

class LyricAdminModel(admin.ModelAdmin):
    readonly_fields=[
        'slug',
        'published',
        'updated'
    ]

admin.site.register(Lyric, LyricAdminModel)
