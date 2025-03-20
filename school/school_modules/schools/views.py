from rest_framework.viewsets import ModelViewSet
from school_modules.schools.models import School
from school_modules.schools.serilaizers import SchoolSerilaizer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerilaizer
