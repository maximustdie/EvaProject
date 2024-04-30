from rest_framework import serializers

from .models import CPULoad


class CPULoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPULoad
        fields = ['id', 'pub_date', 'load']

    def create(self, validated_data):

        return CPULoad.objects.create(**validated_data)
