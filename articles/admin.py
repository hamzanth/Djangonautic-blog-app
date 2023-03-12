from django.contrib import admin
from .models import Articles, Comment, Reply
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "author", "date", "article")
	list_display_links = ("id", "title")
	search_fields = ("name", "author")
	list_per_page = 15

class ArticlesAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "author", "date")
	list_display_links = ("id", "title")
	search_fields = ("name", "author")
	list_filter = ("title", "author")
	# list_editable = ("title",)
	list_per_page = 15

class ReplyAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "author", "article", "date")
	list_display_links = ("id", "title")
	search_fields = ("name", "author")
	list_filter = ("title", "author")
	# list_editable = ("title",)
	list_per_page = 15

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)