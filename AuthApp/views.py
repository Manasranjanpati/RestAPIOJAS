from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from AuthApp.models import AssetData
from AuthApp.serialzers import AssetSerialzers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class AssetViewSet(ModelViewSet):
    queryset = AssetData.objects.all()
    serializer_class = AssetSerialzers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]

