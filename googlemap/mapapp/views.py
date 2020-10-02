from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')