from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.encode, name="encode"),
    path('shortened-url/<int:link_id>', views.new_url, name="new_url"),
    path('decode/', views.decode, name="decode")
]
