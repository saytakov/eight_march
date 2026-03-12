from django.contrib import admin

from .models import Postcard, Recepient


@admin.register(Recepient)
class RecepientAdmin(admin.ModelAdmin):
    """Регистрация полей для админ-панели для получателей."""
    list_display = ('name', 'slug')


@admin.register(Postcard)
class PostcardAdmin(admin.ModelAdmin):
    """Регистрация полей для админ-панели для открыток."""
    list_display = ('recepient', 'path_image', 'description')
