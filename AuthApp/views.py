from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from AuthApp.models import AssetData
from AuthApp.serialzers import AssetSerialzers

class AssetViewSet(ModelViewSet):
    queryset = AssetData.objects.all()
    serializer_class = AssetSerialzers