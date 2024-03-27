from django.urls import path
from .views import AlunosView, AlunosGetView, AlunoListUpdateDeleteView


urlpatterns = [
    path("aluno/<uuid:professor_id>/", AlunosView.as_view()),
    path("aluno/", AlunosGetView.as_view()),
    path("alunoID/<uuid:aluno_id>/", AlunoListUpdateDeleteView.as_view()),
]
