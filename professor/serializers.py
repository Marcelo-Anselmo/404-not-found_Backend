from rest_framework import serializers
from .models import Professor
from django.utils import timezone


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
        read_only_fields = ["id", "created_at", "is_active", "alunos"]
        depth = 1

    def format_date_america(self, instance):
        data = super().to_representation(instance)
        data["datetime_field"] = instance.datetime_field.astimezone(
            timezone.get_current_timezone()
        ).strftime("%d/%m/%Y %H:%M:%S")
        return data

    def create(self, validated_data: dict) -> Professor:
        professor = Professor.objects.create(**validated_data)

        return professor

    def update(self, instance: Professor, validated_data: dict) -> Professor:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
