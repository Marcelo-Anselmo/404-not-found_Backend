from django.db import models
import uuid
from professor.models import Professor


class Alunos(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    nome = models.CharField(max_length=60)
    curso = models.CharField(max_length=100)
    RA = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="alunos"
    )
