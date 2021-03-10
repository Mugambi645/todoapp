from django.urls import path,re_path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path('remove/<int:item_id>/',views.remove, name="remove"),
]
