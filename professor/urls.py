from django.urls import path
from .views import CreateProfessor, ListProfessor, ProfessorListUpdateDeleteAPIView

urlpatterns = [
    path("professor/", CreateProfessor.as_view()),
    path("listprofessor/", ListProfessor.as_view()),
    path("professor/<uuid:professor_id>/", ProfessorListUpdateDeleteAPIView.as_view()),
]
