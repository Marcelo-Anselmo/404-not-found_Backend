from rest_framework import serializers
from .models import Professor
from django.utils import timezone
from datetime import datetime


class ProfessorSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

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
        read_only_fields = ["id", "created_at", "is_active"]
        depth = 1

    def format_date_america(self, instance):
        data = super().to_representation(instance)
        data["datetime_field"] = instance.datetime_field.astimezone(
            timezone.get_current_timezone()
        ).strftime("%d/%m/%Y %H:%M:%S")
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for aluno_data in representation["alunos"]:

            if isinstance(aluno_data["created_at"], str):
                aluno_data["created_at"] = datetime.strptime(
                    aluno_data["created_at"], "%Y-%m-%dT%H:%M:%S.%f%z"
                )
            aluno_data["created_at"] = aluno_data["created_at"].strftime(
                "%d/%m/%Y %H:%M:%S"
            )
        return representation

    def create(self, validated_data: dict) -> Professor:
        professor = Professor.objects.create(**validated_data)

        return professor

    def update(self, instance: Professor, validated_data: dict) -> Professor:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
