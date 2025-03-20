from rest_framework.routers import SimpleRouter
from school_modules.schools.views import SchoolViewSet

from school.settings import REGULAR_API_PREFIX

router = SimpleRouter()
router.register(f"{REGULAR_API_PREFIX}schools", SchoolViewSet)

urlpatterns = router.urls
