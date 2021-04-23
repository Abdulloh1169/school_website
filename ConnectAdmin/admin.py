from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import reverse
from base import models


@admin.register(models.MailToAdmin)
class MyAdmin(admin.ModelAdmin):
    list_display = ("func",)

    def has_add_permission(self, request, obj=None):
        return False

    def func(self, obj):
        return format_html("<a href={}>messages", reverse("contact_admin"))

    func.short_description = "link to messages"