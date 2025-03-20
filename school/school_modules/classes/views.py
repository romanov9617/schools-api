from rest_framework.viewsets import ModelViewSet
from school_modules.classes.models import Class
from school_modules.classes.serilaizers import ClassSerializer
from school_modules.classes.serilaizers import OneClassSerializer
from school_modules.core.views.mixins import ListViewSetMixin


class ClassViewSet(ListViewSetMixin, ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = OneClassSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ClassSerializer
        return super().get_serializer_class()
