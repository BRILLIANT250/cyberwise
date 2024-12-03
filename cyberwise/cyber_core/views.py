from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CybersecurityContent
from .serializers import CybersecurityContentSerializer
# Create your views here.
class CyberContentAPIView(APIView):
    def get(self, request):
        contents = CybersecurityContent.objects.all()
        serializer = CybersecurityContentSerializer(contents, many=True)
        return Response(serializer.data)