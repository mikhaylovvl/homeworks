from django.urls import path

from articles.views import articles_list, tags_list

urlpatterns = [
    path('', articles_list, name='articles'),
    path('articles/tag', tags_list),
]
