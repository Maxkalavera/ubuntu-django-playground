from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    # in case of user admin of django
    # url(r'^admin/', admin.site.urls),
    # This is an example of including a namespace that will extend of this
    # url(r'^$', index, name='index')
    # This is an example of including a function view
    # url(r'^$', Index.as_view(), name='index')
    # this is an exammple of including a generic class based view
    # url(r'^namespace/$', include('namespace.urls', namespace='namespace'))
]
