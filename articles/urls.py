from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = "articles"

urlpatterns = [
    path("", views.article_list, name="list"),
    path("create", views.article_create, name="create"),
    path("<str:slug>", views.article_detail, name="detail"),
    path("<str:slug>/delete", views.article_delete, name="delete"),
    path("<str:slug>/update", views.article_update, name="update"),
    path("<str:slug>/comment", views.article_comment, name="article_comment"),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)