from rest_framework.routers import SimpleRouter
from school_modules.pupils.views import PupilViewSet

from school.settings import REGULAR_API_PREFIX

router = SimpleRouter()
router.register(f"{REGULAR_API_PREFIX}pupils", PupilViewSet)

urlpatterns = router.urls
