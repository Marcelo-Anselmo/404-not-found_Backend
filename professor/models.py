from django.db import models
import uuid


class Professor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(max_length=60)
    email = models.CharField(max_length=200)
    disciplina = models.CharField(max_length=100)
    turno = models.CharField(max_length=60)
    aula = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200, null=True)
