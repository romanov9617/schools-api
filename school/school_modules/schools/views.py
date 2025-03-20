from rest_framework.viewsets import ModelViewSet
from school_modules.core.views.mixins import ListViewSetMixin
from school_modules.schools.models import School
from school_modules.schools.serilaizers import OneSchoolSerilaizer
from school_modules.schools.serilaizers import SchoolSerilaizer


class SchoolViewSet(ListViewSetMixin, ModelViewSet):
    queryset = School.objects.all()
    serializer_class = OneSchoolSerilaizer

    def get_serializer_class(self):
        if self.action == "list":
            return SchoolSerilaizer
        return super().get_serializer_class()
