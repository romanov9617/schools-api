from rest_framework.serializers import ModelSerializer
from school_modules.pupils.models import Pupil


class PupilSerilizer(ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"
