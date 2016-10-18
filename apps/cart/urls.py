from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^add$', views.add_to_cart),
    url(r'^delete$', views.delete_from_cart),
    url(r'^clear$', views.clear_carts),
    url(r'^getlist$', views.getlist),
)
