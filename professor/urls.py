from django.urls import path
from .views import (
    CreateProfessor,
    ListProfessor,
    ProfessorListUpdateDeleteAPIView,
    Created_PDF_View,
)

urlpatterns = [
    path("professor/", CreateProfessor.as_view()),
    path("listprofessor/", ListProfessor.as_view()),
    path("professor/<uuid:professor_id>/", ProfessorListUpdateDeleteAPIView.as_view()),
    path("send_email/<uuid:professor_id>/", Created_PDF_View.as_view()),
]
