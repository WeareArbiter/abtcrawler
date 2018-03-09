from rest_framework import serializers
from project.models import RequestForm

class RequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForm
        fields = ('id',
                'timestamp',
                'name',
                'phone',
                'email',
                'start_date',
                'end_date',
                'datatype',
                'estimate_price',
                'real_price',
                'description',
                )
