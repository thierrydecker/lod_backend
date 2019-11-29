from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

admin.site.site_header = 'LOD Administration'
admin.site.site_title = 'LOD'
admin.site.index_title = 'Topics'

urlpatterns = [
    re_path(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('grappelli/', include('grappelli.urls')),
    path('backendmin/', admin.site.urls),
    path('', include('api.applications.rest.urls')),
]
