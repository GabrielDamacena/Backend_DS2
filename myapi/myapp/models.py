from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    foto = models.ImageField(upload_to='usuarios/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Ponto(models.Model):
    STATUS_CHOICES = [
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
    ]
    
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    lat_long = models.CharField(max_length=50)  # Exemplo: "latitude, longitude"
    data_hora = models.DateTimeField()
    temp_photo = models.ImageField(upload_to='temp_photos/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reconhecido = models.BooleanField(default=True, help_text="Indica se o usuário foi reconhecido com sucesso")
    distancia = models.FloatField(null=True, blank=True, help_text="Distância do reconhecimento facial para análise")


    def __str__(self):
        if self.user:
            return f"Ponto {self.get_status_display()} - {self.user.nome} - {self.data_hora}"
        return f"Ponto {self.get_status_display()} - Usuário Desconhecido - {self.data_hora}"

