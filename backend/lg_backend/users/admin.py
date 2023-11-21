from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.image.url,
            width=obj.image.width,
            height=obj.image.height,
        )
        )


admin.site.register(CustomUser, CustomUserAdmin)
