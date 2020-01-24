# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import dashBourdBd, ticketChat


@admin.register(dashBourdBd)
class dashBourdBdAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'data',
        'title',
        'content',
        'autors',
        'priority',
        'types',
        'status',
        'File',
    )
    list_filter = ('data',)


@admin.register(ticketChat)
class ticketChatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'post',
        'name',
        'body',
        'created',
        'updated',
    )
    list_filter = ('post', 'created', 'updated',)
    search_fields = ('name',)
