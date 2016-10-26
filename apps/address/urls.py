from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.address),
    url(r'^add$', views.add_one_address),
    url(r'^delete$', views.delete_one_address),
    # url(r'^get_goods_info$', views.get_goods_info),
    # url(r'^update$', views.update_one_goods),
    # url(r'^get$', views.get_one_goods),
    url(r'^getlist$', views.getlist),
    # url(r'^search$', views.search),
)
