from .serializers import ExchangeRateSerializer
from .models import ExchangeRate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def exchange_rate(request):
    if request.method == 'GET':
        charcode = request.query_params.get('charcode')
        date = request.query_params.get('date')
        if charcode and date:
            q = ExchangeRate.objects.filter(charcode=charcode, date=date)
        elif charcode:
            q = ExchangeRate.objects.filter(charcode=charcode)
        elif date:
            q = ExchangeRate.objects.filter(date=date)
        else:
            q = ExchangeRate.objects.all()
        serializer = ExchangeRateSerializer(q, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = ExchangeRateSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
