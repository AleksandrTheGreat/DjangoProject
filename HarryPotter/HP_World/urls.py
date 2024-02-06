from django.urls import path
from . import views
# import HP_World.views as views

urlpatterns = [
    path('', views.main, name='main')
]
