from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('parents/', views.ParentList.as_view()),
    path('parents/<uuid:pk>/', views.ParentDetail.as_view()),
    path('children/', views.ChildList.as_view()),
    path('children/<uuid:pk>/', views.ChildDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
