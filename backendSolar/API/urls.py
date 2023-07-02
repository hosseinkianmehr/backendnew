from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path("blog/", views.listblog.as_view(), name="listview"),
    path("news/", views.listnews.as_view(), name="listview"),
    path("youtube/", views.listyoutube.as_view(), name="listview"),
    path("blog/<int:pk>/", views.detailblog.as_view(), name="blog-detali"),
    path("news/<int:pk>/", views.detailnews.as_view(), name="news-detali"),
    path("youtube/<int:pk>/", views.detailyoutube.as_view(), name="youtube-detail"),
    #home
    path("home/", views.Home.as_view(), name="Home"),
]