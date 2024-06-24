from django.urls import path
from . import views

urlpatterns = [
    # Aluno URLs
    path('alunos/', views.aluno_list, name='aluno-list'),
    path('alunos/<int:pk>/', views.aluno_detail, name='aluno-detail'),
    path('alunos/search/', views.aluno_search, name='aluno-search'),

    # Professor URLs
    path('professores/', views.professor_list, name='professor-list'),
    path('professores/<int:pk>/', views.professor_detail, name='professor-detail'),
    path('professores/search/', views.professor_search, name='professor-search'),

    # Curso URLs
    path('cursos/', views.curso_list, name='curso-list'),
    path('cursos/<int:pk>/', views.curso_detail, name='curso-detail'),
    path('cursos/search/', views.curso_search, name='curso-search'),

    # Additional Functionalities
    path('alunos/<int:pk>/matriculas/', views.aluno_matriculas, name='aluno-matriculas'),
    path('professores/<int:pk>/cursos/', views.professor_cursos, name='professor-cursos'),
    path('cursos/<int:pk>/alunos/', views.curso_alunos, name='curso-alunos'),
]
