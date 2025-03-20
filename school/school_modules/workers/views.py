from rest_framework.viewsets import ModelViewSet
from school_modules.core.views.mixins import ListViewSetMixin
from school_modules.workers.models import Worker
from school_modules.workers.serilaizers import OneWorkerSerializer
from school_modules.workers.serilaizers import WorkerSerializer


class WorkerViewSet(ListViewSetMixin, ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = OneWorkerSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return WorkerSerializer
        return super().get_serializer_class()
