from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path("list/", views.listapiview.as_view(), name="listview")
]