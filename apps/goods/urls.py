from django.conf.urls import url, patterns, include
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home_list_page),
    url(r'^detail/(\d+)$', views.goods_detail),
    url(r'^list/(?P<goods_type_id>\d+)/(?P<page>\d+)$', views.goods_list),
    # url(r'^add$', views.add_one_goods),
    # url(r'^delete$', views.delete_one_goods),
    url(r'^get_goods_info$', views.get_goods_info),
    # url(r'^update$', views.update_one_goods),
    url(r'^get$', views.get_one_goods),
    url(r'^getlist$', views.getlist),
    # url(r'^search$', views.search),
    url(r'^search$', views.MySearchView.as_view()),
    # url(r'^search/', include('haystack.urls')),
)
