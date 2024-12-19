from django.urls import path
from . import views as v

urlpatterns = [
    path('show/', v.show, name='show'),
    path('', v.create, name='create'),
    path('update/<int:pk>/', v.update, name='update'),
    path('delete/<int:pk>/', v.delete, name='delete'),
    path('search/', v.search, name='search'),
]
