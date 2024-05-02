from rest_framework.serializers import ModelSerializer
from .models import ExchangeRate


class ExchangeRateSerializer(ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('charcode', 'date', 'rate')
