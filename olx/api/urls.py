from django.contrib import admin
from django.urls import path, include, re_path
from .viewsets import *

urlpatterns = [
    path(r'olx/all/',  AllViewSet.as_view({'get':'list'})),
    re_path(r'^olx/category/(?P<category>[\w]+)/$', CategoryViewSet.as_view()),
    re_path(r'^olx/detail/(?P<pk>[0-9])/$', ProductDetailViewSet.as_view()),
    
]

