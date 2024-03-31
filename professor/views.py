from .models import Professor
from aluno.models import Alunos
from .serializers import ProfessorSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from send_email import created_pdf


class CreateProfessor(CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


class ListProfessor(ListAPIView):
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        return Professor.objects.filter(is_active=True)


class ProfessorListUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    lookup_url_kwarg = "professor_id"


class Created_PDF_View(RetrieveAPIView):
    serializer_class = ProfessorSerializer
    lookup_url_kwarg = "professor_id"

    def get_queryset(self):
        professor = Professor.objects.filter(id=self.kwargs.get("professor_id"))
        alunos = Alunos.objects.filter(professor=self.kwargs.get("professor_id"))
        created_pdf(professor, alunos)
        return professor
