from django.conf.urls import url 
from BookShelfApp.views import user, book


urlpatterns=[
    url(r'^user/$', user.userApi),
    url(r'^user/([0-9]+)$', user.userApi),
    url(r'^book/$', book.bookApi),
    url(r'^book/([0-9]+)$', book.bookApi)
]