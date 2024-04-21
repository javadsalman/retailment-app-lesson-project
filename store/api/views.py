from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import StoreSerializer
from ..models import Store

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer

    def get_queryset(self): # type: ignore
        return Store.objects.filter(deleted=False, customer=self.request.user.customer) # type: ignore
    def get_serializer_context(self):
        return super().get_serializer_context()
    
    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
