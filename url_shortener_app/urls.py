from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('encode/<int:link_id>', views.encode, name="encode"),
    path('decode/<int:link_id>', views.decode, name="decode")
]
