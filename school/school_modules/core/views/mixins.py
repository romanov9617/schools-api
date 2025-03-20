from rest_framework.response import Response


class ListViewSetMixin:
    def list(self, request, *args, **kwargs):
        resp = super().list(request, *args, **kwargs)
        return Response({"list": resp.data})
