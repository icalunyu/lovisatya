from django.contrib import admin
from django.urls import path
from cms.views import index, thanks, dresscode, validate_code
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from lovigraha import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('thanks', thanks, name='thanks'),
    path('dresscode', dresscode, name='dresscode'),

    url(r'^ajax/validate_code/$', validate_code, name='validate_code'),
]

urlpatterns += staticfiles_urlpatterns()
