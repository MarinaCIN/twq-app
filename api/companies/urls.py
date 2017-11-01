from django.conf.urls import url, include

from .views import TeamView, CompanyView

urlpatterns = [
    url(r'^(?P<company_id>\w+)/team/$', TeamView.as_view(), name="teams"),
    url(r'^(?P<company_id>\w+)/team/(?P<team_id>\w+)$', TeamView.as_view(), name="get_team"),
    url(r'^(?P<company_id>\w+)/forms/', include('forms.urls')),
    url(r'^$', CompanyView.as_view(), name="companies"),
]