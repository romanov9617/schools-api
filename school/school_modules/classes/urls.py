from rest_framework.routers import SimpleRouter
from school_modules.classes.views import ClassViewSet

from school.settings import REGULAR_API_PREFIX

router = SimpleRouter()
router.register(f"{REGULAR_API_PREFIX}classes", ClassViewSet)

urlpatterns = router.urls
