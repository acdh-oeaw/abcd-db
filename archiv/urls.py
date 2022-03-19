# generated by appcreator
from django.conf.urls import url
from . import views
from archiv.data_views import event_calendar_data, EventCalendarView

app_name = 'archiv'
urlpatterns = [
    url(
        r'^event-calendar-data/$',
        event_calendar_data,
        name='event_calendar_data'
    ),
    url(
        r'^event-calendar/$',
        EventCalendarView.as_view(),
        name='event_calendar'
    ),
    url(
        r'^event/$',
        views.EventListView.as_view(),
        name='event_browse'
    ),
    url(
        r'^event/detail/(?P<pk>[0-9]+)$',
        views.EventDetailView.as_view(),
        name='event_detail'
    ),
    url(
        r'^event/create/$',
        views.EventCreate.as_view(),
        name='event_create'
    ),
    url(
        r'^event/edit/(?P<pk>[0-9]+)$',
        views.EventUpdate.as_view(),
        name='event_edit'
    ),
    url(
        r'^event/delete/(?P<pk>[0-9]+)$',
        views.EventDelete.as_view(),
        name='event_delete'),
    url(
        r'^work/$',
        views.WorkListView.as_view(),
        name='work_browse'
    ),
    url(
        r'^work/detail/(?P<pk>[0-9]+)$',
        views.WorkDetailView.as_view(),
        name='work_detail'
    ),
    url(
        r'^work/create/$',
        views.WorkCreate.as_view(),
        name='work_create'
    ),
    url(
        r'^work/edit/(?P<pk>[0-9]+)$',
        views.WorkUpdate.as_view(),
        name='work_edit'
    ),
    url(
        r'^work/delete/(?P<pk>[0-9]+)$',
        views.WorkDelete.as_view(),
        name='work_delete'),
    url(
        r'^wab/$',
        views.WabListView.as_view(),
        name='wab_browse'
    ),
    url(
        r'^wab/detail/(?P<pk>[0-9]+)$',
        views.WabDetailView.as_view(),
        name='wab_detail'
    ),
    url(
        r'^wab/create/$',
        views.WabCreate.as_view(),
        name='wab_create'
    ),
    url(
        r'^wab/edit/(?P<pk>[0-9]+)$',
        views.WabUpdate.as_view(),
        name='wab_edit'
    ),
    url(
        r'^wab/delete/(?P<pk>[0-9]+)$',
        views.WabDelete.as_view(),
        name='wab_delete'),
    url(
        r'^person/$',
        views.PersonListView.as_view(),
        name='person_browse'
    ),
    url(
        r'^person/detail/(?P<pk>[0-9]+)$',
        views.PersonDetailView.as_view(),
        name='person_detail'
    ),
    url(
        r'^person/create/$',
        views.PersonCreate.as_view(),
        name='person_create'
    ),
    url(
        r'^person/edit/(?P<pk>[0-9]+)$',
        views.PersonUpdate.as_view(),
        name='person_edit'
    ),
    url(
        r'^person/delete/(?P<pk>[0-9]+)$',
        views.PersonDelete.as_view(),
        name='person_delete'
    ),
    url(
        r'^place/$',
        views.PlaceListView.as_view(),
        name='place_browse'
    ),
    url(
        r'^place/detail/(?P<pk>[0-9]+)$',
        views.PlaceDetailView.as_view(),
        name='place_detail'
    ),
    url(
        r'^place/create/$',
        views.PlaceCreate.as_view(),
        name='place_create'
    ),
    url(
        r'^place/edit/(?P<pk>[0-9]+)$',
        views.PlaceUpdate.as_view(),
        name='place_edit'
    ),
    url(
        r'^place/delete/(?P<pk>[0-9]+)$',
        views.PlaceDelete.as_view(),
        name='place_delete'
    ),
    url(
        r'^institution/$',
        views.InstitutionListView.as_view(),
        name='institution_browse'
    ),
    url(
        r'^institution/detail/(?P<pk>[0-9]+)$',
        views.InstitutionDetailView.as_view(),
        name='institution_detail'
    ),
    url(
        r'^institution/create/$',
        views.InstitutionCreate.as_view(),
        name='institution_create'
    ),
    url(
        r'^institution/edit/(?P<pk>[0-9]+)$',
        views.InstitutionUpdate.as_view(),
        name='institution_edit'
    ),
    url(
        r'^institution/delete/(?P<pk>[0-9]+)$',
        views.InstitutionDelete.as_view(),
        name='institution_delete'
    ),
]
