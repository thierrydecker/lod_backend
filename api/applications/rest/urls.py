from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('parents/', views.parent_list),
    path('parents/<uuid:pk>/', views.parent_detail),
    path('children/', views.child_list),
    path('children/<uuid:pk>/', views.child_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
