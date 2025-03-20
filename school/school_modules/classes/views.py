from rest_framework.viewsets import ModelViewSet
from school_modules.classes.models import Class
from school_modules.classes.serilaizers import ClassSerializer


class ClassViewSet(ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
