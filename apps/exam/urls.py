from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^add_wish_page$', views.add_wish_page),
    url(r'^add_wish$', views.add_wish),
    url(r'^wish_page/(?P<wish_id>\d+)$', views.wish_page),

    url(r'^add_to_wishes/(?P<wish_id>\d+)$', views.add_to_wishes),
    url(r'^remove/(?P<wish_id>\d+)$', views.remove_wish),

    url(r'^delete/(?P<wish_id>\d+)$', views.delete_wish),
]
