from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from archiv import api_views as archiv_api_views

router = routers.DefaultRouter()
router.register(r"events", archiv_api_views.EventViewSet)
router.register(r"works", archiv_api_views.WorkViewSet)
router.register(r"persons", archiv_api_views.PersonViewSet)
router.register(r"places", archiv_api_views.PlaceViewSet)
router.register(r"institutions", archiv_api_views.InstitutionViewSet)
router.register(r"wabs", archiv_api_views.WabViewSet)


urlpatterns = [
    path("api/", include(router.urls), name="api-root"),
    path("admin/", admin.site.urls),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("archiv-ac/", include("archiv.dal_urls", namespace="archiv-ac")),
    path("vocabs/", include("vocabs.urls", namespace="vocabs")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("", include("webpage.urls", namespace="webpage")),
    path("infos/", include("infos.urls", namespace="infos")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "webpage.views.handler404"
