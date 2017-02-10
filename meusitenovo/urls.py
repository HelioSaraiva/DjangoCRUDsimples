from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'meusitenovo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'cliente.views.home', name='cliente_home'),
    url(r'^cliente/$', 'cliente.views.cliente', name='cliente_principal'),
    url(r'^cliente_novo/$', 'cliente.views.create', name='cliente_create'),
    url(r'^cliente_delete/(?P<pk>\d+)/$', 'cliente.views.delete', name='cliente_delete'),
    url(r'^cliente/(?P<pk>\d+)/$', 'cliente.views.cliente_update', name='cliente_update'),
    url(r'^admin/', include(admin.site.urls)),
]    
        