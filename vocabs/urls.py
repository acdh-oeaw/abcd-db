from django.urls import path
from . import views


app_name = "vocabs"
urlpatterns = [
    path("skosconcept", views.SkosConceptListView.as_view(), name="skosconcept_browse"),
    path(
        "skosconcept/detail/<int:pk>",
        views.SkosConceptDetailView.as_view(),
        name="skosconcept_detail",
    ),
    path(
        "skosconcept/create",
        views.SkosConceptCreate.as_view(),
        name="skosconcept_create",
    ),
    path(
        "skosconcept/edit/<int:pk>",
        views.SkosConceptUpdate.as_view(),
        name="skosconcept_edit",
    ),
    path(
        "skosconcept/delete/<int:pk>",
        views.SkosConceptDelete.as_view(),
        name="skosconcept_delete",
    ),
    path(
        "skoscollection",
        views.SkosCollectionListView.as_view(),
        name="skoscollection_browse",
    ),
    path(
        "skoscollection/detail/<int:pk>",
        views.SkosCollectionDetailView.as_view(),
        name="skoscollection_detail",
    ),
    path(
        "skoscollection/create",
        views.SkosCollectionCreate.as_view(),
        name="skoscollection_create",
    ),
    path(
        "skoscollection/edit/<int:pk>",
        views.SkosCollectionUpdate.as_view(),
        name="skoscollection_edit",
    ),
    path(
        "skoscollection/delete/<int:pk>",
        views.SkosCollectionDelete.as_view(),
        name="skoscollection_delete",
    ),
    path(
        "skostechnicalcollection",
        views.SkosTechnicalCollectionListView.as_view(),
        name="skostechnicalcollection_browse",
    ),
    path(
        "skostechnicalcollection/detail/<int:pk>",
        views.SkosTechnicalCollectionDetailView.as_view(),
        name="skostechnicalcollection_detail",
    ),
    path(
        "skostechnicalcollection/create",
        views.SkosTechnicalCollectionCreate.as_view(),
        name="skostechnicalcollection_create",
    ),
    path(
        "skostechnicalcollection/edit/<int:pk>",
        views.SkosTechnicalCollectionUpdate.as_view(),
        name="skostechnicalcollection_edit",
    ),
    path(
        "skostechnicalcollection/delete/<int:pk>",
        views.SkosTechnicalCollectionDelete.as_view(),
        name="skostechnicalcollection_delete",
    ),
]
