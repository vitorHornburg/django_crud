from django.contrib import admin
from .models import Aluno, Professor, Curso, Departamento, Sala, Matricula, Alocacao, CursoSala

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Departamento)
admin.site.register(Sala)
admin.site.register(Matricula)
admin.site.register(Alocacao)
admin.site.register(CursoSala)
