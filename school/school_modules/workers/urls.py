from rest_framework.routers import SimpleRouter
from school_modules.workers.views import WorkerViewSet

from school.settings import REGULAR_API_PREFIX

router = SimpleRouter()
router.register(f"{REGULAR_API_PREFIX}workers", WorkerViewSet)

urlpatterns = router.urls
