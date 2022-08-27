from rest_framework.routers import DefaultRouter

from airlines.views import AirplanesViewSet


router = DefaultRouter()

router.register(prefix='airplanes', viewset=AirplanesViewSet)

urlpatterns = router.urls
