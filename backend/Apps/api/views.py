import json
from products.models import Product
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request, *arg, **kwargs):
    # if request.method != 'POST':
    #     return Response({'detail': 'Method get not allowed!!!'}, status=405)
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        instance = serializer.save()

        print("SALOM")
        data = ProductSerializer(instance).data
    return Response(data)
