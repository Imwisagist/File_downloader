from rest_framework import mixins, viewsets

from .models import File
from .serializers import FileSerializer


class FileViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """
    The viewset for processing requests to download a file 
    and get a list of all files with defaulth pagination
    """

    queryset = File.objects.all()
    serializer_class = FileSerializer
