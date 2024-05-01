from .models import Alunos
from professor.models import Professor
from .serializers import AlunoSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.exceptions import APIException
from rest_framework import status
from django.shortcuts import get_object_or_404


class GetAluno(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class GetProfessor(APIException):
    status_code = status.HTTP_400_BAD_REQUEST


class AlunosView(CreateAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

    lookup_url_kwarg = "professor_id"

    def perform_create(self, serializer):
        professor_found = Professor.objects.filter(id=self.kwargs.get("professor_id"))

        if not professor_found:
            raise GetProfessor("O ID do professor não existe")

        professor = get_object_or_404(Professor, id=self.kwargs.get("professor_id"))

        alunos = list(professor.alunos.values())
        request = self.request.data

        for aluno in alunos:
            if request["RA"] == aluno["RA"]:
                raise GetAluno("Aluno ja registrado!")

        serializer.save(professor=professor)


class AlunosGetView(ListAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer


class AlunoListUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

    lookup_url_kwarg = "aluno_id"
