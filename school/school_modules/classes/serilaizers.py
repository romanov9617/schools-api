from rest_framework.serializers import ModelSerializer
from school_modules.classes.models import Class
from school_modules.core.serializers.mixins import OneEntityMixin


class ClassSerializer(ModelSerializer):
    class Meta:
        model = Class
        fields = "__all__"


class OneClassSerializer(OneEntityMixin, ClassSerializer):
    pass
