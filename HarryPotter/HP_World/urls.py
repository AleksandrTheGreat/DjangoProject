from django.urls import path
from . import views
# import HP_World.views as views

urlpatterns = [
    path('', views.main, name='main'),
    path('foundation/<str:page>/', views.foundation, name='foundation'),
    path('elements/<str:section>/', views.elements, name='elements'),
    path('info/<str:id>/', views.info, name='info'),
    path('grimoire/', views.grimoire, name='grimoire'),
    path('shop/', views.shop, name='shop')
]
