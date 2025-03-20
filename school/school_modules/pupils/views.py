from rest_framework.viewsets import ModelViewSet
from school_modules.pupils.models import Pupil
from school_modules.pupils.serializers import PupilSerilizer


class PupilViewSet(ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerilizer
