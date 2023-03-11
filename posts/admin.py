from django.contrib import admin

from users.models import Contact

from .models import Comment, Post, Space

admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "link",
        "tags",
        "labels",
        "text",
        "created_date",
        "status",
    ]
    list_filter = ["status", "created_date", "author"]
    search_fields = ["title", "text", "tags", "labels"]
    raw_id_fields = ["author"]
    date_hierarchy = "created_date"
    ordering = ["status", "publish"]


admin.site.register(Comment)
admin.site.register(Space)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "created_date", "approved_comment")
    list_filter = ("created_date", "post")
    search_fields = ("author", "post", "text")


# admin.site.register(Author)
#
#
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'photo']

admin.site.register(Contact)
