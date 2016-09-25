
from django.conf.urls import url
from django.contrib import admin
from uploads import views as up_views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^up/$', up_views.index, name="up"),
]
