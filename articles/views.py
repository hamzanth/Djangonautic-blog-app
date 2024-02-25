from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Articles, Comment
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse

# Create your views here.
def article_list(request):
	#return HttpResponse("this is the article list page")
	articles = Articles.objects.all().order_by("date")
	context = {
		"articles": articles,
	}
	return render(request, "articles/article_list.html", context)

def article_detail(request, slug):
	# return HttpResponse(slug)
	# article = Articles.objects.get(slug=slug)
	article = get_object_or_404(Articles, slug=slug)
	print(article.thumb.url)
	comments = article.comments.all()
	context = {
		"article": article,
		"comments": comments
	}
	return render(request, "articles/article_detail.html", context)

@login_required(login_url="/account/login")
def article_create(request):
	if request.method == "POST":
		form = forms.CreateArticle(request.POST, request.FILES)
		if form.is_valid():
			#save to db
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect("articles:list")
	else:
		form = forms.CreateArticle()
	return render(request, "articles/article_create.html", {"form":form})

@login_required(login_url="/accounts/login")
def article_update(request, slug):
	# return HttpResponse("This is the Updating page")
	article = Articles.objects.get(slug=slug)
	if request.method == "POST":
		form = forms.CreateArticle(request.POST, instance=article)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("articles:detail", args=(article.slug,)))
	else:
		form = forms.CreateArticle(instance=article)
	return render(request, "articles/article_update.html", {"form":form, "article":article})

@login_required(login_url="/accounts/login")
def article_delete(request, slug):
	article = Articles.objects.get(slug=slug)
	if request.method == "POST":
		article.delete()
		return redirect("articles:list")
	else:
		return render(request, "articles/article_delete.html", {"article":article})

def article_comment(request, slug):
	if request.POST:
		title = request.POST.get("title")
		author = request.user
		article = get_object_or_404(Articles, slug=slug)
		# if request.user is None:
		# 	author = "Anonymous"
		comment = Comment(title=title, author=author, article=article)
		comment.save()
		return HttpResponseRedirect(reverse("articles:detail", args=(article.slug,)))