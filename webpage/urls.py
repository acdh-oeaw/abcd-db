from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from archiv import search_result_views
from django_spaghetti.views import Plate
from archiv.views import EventDetailView

app_name = "webpage"

favicon_view = RedirectView.as_view(url="/static/favicon.ico", permanent=True)

urlpatterns = [
    path("imprint/", views.ImprintView.as_view(), name="imprint"),
    path(
        "data-model/",
        Plate.as_view(plate_template_name="webpage/data_model.html"),
        name="data_model",
    ),
    path("", views.GenericWebpageView.as_view(), name="start"),
    path("<int:pk>", EventDetailView.as_view(), name="event_pid"),
    path("<int:pk>/", EventDetailView.as_view(), name="event_pid_slash"),
    path("results/", search_result_views.EventResultView.as_view(), name="results"),
    path("accounts/login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("project-info/", views.project_info, name="project_info"),
    path("<slug:template>/", views.GenericWebpageView.as_view(), name="staticpage"),
]
