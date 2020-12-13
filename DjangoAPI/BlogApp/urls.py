from django.conf.urls import url
from BlogApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^blogType/$', views.blogTypeApi),
    url(r'^blogType/([0-9]+)$', views.blogTypeApi),

    url(r'^blog/$', views.blogApi),
    url(r'^blog/([0-9]+)$', views.blogApi),

    url(r'^SaveFile$', views.SaveFle)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)