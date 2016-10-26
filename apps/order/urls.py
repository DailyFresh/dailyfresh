from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<page>\d+)$', views.my_order),
    url(r'^commit$', views.commit_order),
    url(r'^add$', views.add_order),
    url(r'^finish$', views.finish_order),
    url(r'^comment$', views.comment),
    url(r'^delete$', views.delete_one_order),
    url(r'^cancel$', views.cancel_one_order),
    # url(r'^get_goods_info$', views.get_goods_info),
    # url(r'^update$', views.update_one_goods),
    # url(r'^get$', views.get_one_goods),
    url(r'^getlist$', views.getlist),
    # url(r'^search$', views.search),
)
