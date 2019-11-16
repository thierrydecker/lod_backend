from django.contrib import admin
from django.urls import include
from django.urls import path

admin.site.site_header = 'LOD Administration'
admin.site.site_title = 'LOD'
admin.site.index_title = 'Topics'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
