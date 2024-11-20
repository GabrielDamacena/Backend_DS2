from rest_framework import serializers
from .models import Usuario, Ponto


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'cargo', 'cpf', 'foto']



class PontoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Exibe o nome de usuário em vez do ID
    status_display = serializers.CharField(source='get_status_display', read_only=True)  # Exibe o texto do status
    distancia = serializers.FloatField(read_only=True)  # Distância é somente leitura

    class Meta:
        model = Ponto
        fields = [
            'id',
            'user',
            'lat_long',
            'data_hora',
            'temp_photo',
            'status',
            'status_display',
            'reconhecido',
            'distancia',
        ]

class PhotoUploadSerializer(serializers.Serializer):
    photo = serializers.ImageField()
