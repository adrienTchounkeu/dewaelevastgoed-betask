"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from articles.views import (
    ArticleDetailAPIView,
    ArticleListCreateAPIView,
    ListArticleByTag,
    TagAddRemoveAPIView,
    TagListCreateAPIView,
    TagUpdateDeleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/articles/", ArticleListCreateAPIView.as_view(), name="article_list"),
    path(
        "api/articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"
    ),
    path("api/tags/", TagListCreateAPIView.as_view(), name="tag_list"),
    path(
        "api/tags/<int:pk>/", TagAddRemoveAPIView.as_view(), name="tag_add_remove"
    ),
    path(
        "api/tags/<int:tag_id>/", ListArticleByTag.as_view(), name="list_tag_article"
    ),
    path(
        "api/tags/update-delete/", TagUpdateDeleteView.as_view(), name="update_delete_tags"
    ),
]
