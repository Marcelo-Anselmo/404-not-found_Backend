from .models import Professor
from .serializers import ProfessorSerializer
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)


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
