from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', 'DTool.views.home'),
    url(r'register', 'DTool.views.register'),
    url(r'login', 'DTool.views.login'),
    url(r'logout', 'DTool.views.logout'),
    url(r'add_auto', 'DTool.views.add_auto'),
    url(r'my_autos', 'DTool.views.my_autos'),
    url(r'^service/(?P<car_id>\d+)$', 'DTool.views.service'),
    url(r'add_service/(?P<car_id>\d+)/$', 'DTool.views.add_service'),
    url(r'cost/(?P<car_id>\d+)/$', 'DTool.views.cost'),
    url(r'add_cost/(?P<car_id>\d+)$', 'DTool.views.add_cost'),
    url(r'^notification/(?P<car_id>\d+)/$', 'DTool.views.notification'),
    url(r'add_notification/(?P<car_id>\d+)$', 'DTool.views.add_notification'),
    url(r'do_notification/(?P<car_id>\d+)/(?P<note_id>\d+)$', 'DTool.views.do_notification'),
    url(r'^mark/(?P<car_id>\d+)/$', 'DTool.views.mark'),
    url(r'add_mark/(?P<car_id>\d+)$', 'DTool.views.add_mark'),
    url(r'^sell/(?P<car_id>\d+)$', 'DTool.views.sell'),
    url(r'unsell/(?P<car_id>\d+)$', 'DTool.views.unsell'),
    url(r'^advertisements$', 'DTool.views.ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

