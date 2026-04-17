from django.shortcuts import render
from .models import Bagan

def home(request):
    bagans = Bagan.objects.all()  # Fetch all Begenas
    return render(request, 'home.html', {'bagans': bagans})

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bagan
from .serializers import BaganSerializer

@api_view(['GET'])
def bagan_list_api(request):
    bagans = Bagan.objects.all()
    serializer = BaganSerializer(bagans, many=True)
    return Response(serializer.data)