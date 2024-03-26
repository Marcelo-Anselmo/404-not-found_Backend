from rest_framework import serializers
from .models import Alunos
from professor.serializers import ProfessorSerializer


class AlunoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    professor = ProfessorSerializer(read_only=True)

    class Meta:
        model = Alunos
        fields = [
            "id",
            "nome",
            "curso",
            "RA",
            "created_at",
            "professor",
        ]
        read_only_fields = ["id", "created_at", "professor"]
        depth = 1

    def create(self, validated_data: dict) -> Alunos:
        aluno = Alunos.objects.create(**validated_data)

        return aluno

    def update(self, instance: Alunos, validated_data: dict) -> Alunos:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
