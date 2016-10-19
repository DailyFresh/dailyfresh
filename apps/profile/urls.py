from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.profile),
    url(r'^update$', views.update_profile),
    url(r'^get$', views.get_profile),
)
