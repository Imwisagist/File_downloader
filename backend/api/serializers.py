from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    """
    The class describes the fields to be returned
    when uploading a file and 
    requesting a list of files.
    """

    class Meta:
        model = File
        fields = ('id', 'file', 'uploaded_at', 'processed')
        read_only_fields = ('processed',)
