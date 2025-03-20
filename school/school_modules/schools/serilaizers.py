from rest_framework.serializers import ModelSerializer
from school_modules.schools.models import School


class SchoolSerilaizer(ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
