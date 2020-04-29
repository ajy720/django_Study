from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "_type",
        "title",
        "view_count",
        "image",
        "created_at",
        "updated_at",
    )

    search_fields = ("title",)
