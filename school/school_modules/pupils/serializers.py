from rest_framework.serializers import ModelSerializer
from school_modules.classes.models import Class
from school_modules.classes.serilaizers import ClassSerializer
from school_modules.core.serializers.mixins import OneEntityMixin
from school_modules.pupils.models import Pupil


class PupilSerilizer(ModelSerializer):
    _class = ClassSerializer()

    def create(self, validated_data):
        class_data = validated_data.pop("_class")
        _class = Class.objects.get_or_create(class_data)[0]
        school = Pupil.objects.create(_class=_class, **validated_data)
        return school

    class Meta:
        model = Pupil
        fields = "__all__"


class OnePupilSerializer(OneEntityMixin, PupilSerilizer):
    pass
