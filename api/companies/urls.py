from django.conf.urls import url, include

urlpatterns = [
    url(r'^(?P<company_id>\w+)/forms/', include('forms.urls')),
]