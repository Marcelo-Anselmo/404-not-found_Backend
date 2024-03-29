from rest_framework import serializers
from .models import Alunos
from professor.serializers import ProfessorSerializer
from django.utils import timezone


class AlunoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    professor = ProfessorSerializer(read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

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
        read_only_fields = ["id", "created_at"]
        depth = 0

    def format_date_america(self, instance):
        data = super().to_representation(instance)
        data["datetime_field"] = instance.datetime_field.astimezone(
            timezone.get_current_timezone()
        ).strftime("%d/%m/%Y %H:%M:%S")
        return data

    def remove_teacher_field(self, instance):
        data = super().to_representation(instance)
        data.pop("professor", None)
        return data

    def create(self, validated_data: dict) -> Alunos:
        aluno = Alunos.objects.create(**validated_data)

        return aluno

    def update(self, instance: Alunos, validated_data: dict) -> Alunos:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
