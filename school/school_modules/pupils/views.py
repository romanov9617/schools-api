from rest_framework.viewsets import ModelViewSet
from school_modules.core.views.mixins import ListViewSetMixin
from school_modules.pupils.models import Pupil
from school_modules.pupils.serializers import OnePupilSerializer
from school_modules.pupils.serializers import PupilSerilizer


class PupilViewSet(ListViewSetMixin, ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = OnePupilSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PupilSerilizer
        return super().get_serializer_class()
