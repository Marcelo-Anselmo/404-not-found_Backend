from rest_framework import serializers
from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Professor
        fields = [
            "id",
            "nome",
            "email",
            "disciplina",
            "aula",
            "is_active",
            "created_at",
            "descricao",
            "alunos",
        ]
        read_only_fields = ["id", "created_at", "is_active", "alunos"]
        depth = 1

    def create(self, validated_data: dict) -> Professor:
        professor = Professor.objects.create(**validated_data)

        return professor

    def update(self, instance: Professor, validated_data: dict) -> Professor:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
