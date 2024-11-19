from rest_framework import generics
from .models import Usuario,Ponto
from .serializers import UsuarioSerializer,PontoSerializer
import cv2
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from deepface import DeepFace
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class UsuarioListCreateView(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PontoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PontoRegistroView(generics.ListCreateAPIView):
    queryset = Ponto.objects.all()
    serializer_class = PontoSerializer
    