from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from . import views


from store.controller import authview
urlpatterns = [
    path('', views.home,name="home"),
    path('collections',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    
    path('register/',authview.register,name="register"),
]

