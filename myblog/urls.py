from django.conf.urls import url, include
from myblog.views import stub_view
from myblog.views import list_view
from myblog.views import detail_view

urlpatterns = [
    url(r'^$',
        list_view,
        name="blog_index"),
    # url(r'^posts/(\d+)/$',
    # stub_view,
    # name="blog_detail"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^posts/(?P<post_id>\d+)/$',
    detail_view,
    name="blog_detail"),
]