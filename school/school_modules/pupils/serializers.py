from rest_framework.serializers import ModelSerializer
from school_modules.core.serializers.mixins import OneEntityMixin
from school_modules.pupils.models import Pupil


class PupilSerilizer(ModelSerializer):
    class Meta:
        model = Pupil
        fields = "__all__"


class OnePupilSerializer(OneEntityMixin, ModelSerializer):
    pass
