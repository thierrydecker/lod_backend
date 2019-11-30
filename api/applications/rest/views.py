from rest_framework import generics
from rest_framework import mixins

from .models import Child
from .models import Parent
from .serializers import ChildSerializer
from .serializers import ParentSerializer


class ParentList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView,
):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ParentDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView

):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ChildList(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        generics.GenericAPIView,
):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ChildDetail(
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        generics.GenericAPIView

):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
