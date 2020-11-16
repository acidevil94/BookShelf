from django.conf.urls import url 
from BookShelfApp.views import user, book,util

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^user/$', user.userApi),
    url(r'^user/([0-9]+)$', user.userApi),

    url(r'^book/$', book.bookApi),
    url(r'^book/([0-9]+)$', book.bookApi),

     url(r'^SaveFile/$', util.SaveFile)

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)