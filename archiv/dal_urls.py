# generated by appcreator
from django.conf.urls import url
from . import dal_views

app_name = 'archiv'
urlpatterns = [
    url(
        r'^event-autocomplete/$',
        dal_views.EventAC.as_view(),
        name='event-autocomplete'
    ),
    url(
        r'^work-autocomplete/$',
        dal_views.WorkAC.as_view(),
        name='work-autocomplete'
    ),
    url(
        r'^wab-autocomplete/$',
        dal_views.WabAC.as_view(),
        name='wab-autocomplete'
    ),
    url(
        r'^person-autocomplete/$',
        dal_views.PersonAC.as_view(),
        name='person-autocomplete'
    ),
    url(
        r'^place-autocomplete/$',
        dal_views.PlaceAC.as_view(),
        name='place-autocomplete'
    ),
    url(
        r'^institution-autocomplete/$',
        dal_views.InstitutionAC.as_view(),
        name='institution-autocomplete'
    ),
]
