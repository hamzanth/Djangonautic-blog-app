from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	thumb = models.ImageField(default="default.jpg", blank=True)
	author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50] + "..."

	def num_comment(self):
		return len(self.comments.all())

	def get_all_comment(self):
		return self.comments.all()

class Comment(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name="comments")
	article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")

	def __str__(self):
		return self.title

class Reply(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, default=None, null=True, on_delete=models.SET_NULL, related_name="replies")
	article = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")

	def __str__(self):
		return self.title