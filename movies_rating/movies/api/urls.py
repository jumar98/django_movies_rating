from rest_framework.routers import SimpleRouter
from movies.api.viewsets import MovieModelViewSet, MovieRateViewSet

router = SimpleRouter()
router.register('movie', MovieModelViewSet)
router.register('movierate', MovieRateViewSet)

urlpatterns = router.urls
