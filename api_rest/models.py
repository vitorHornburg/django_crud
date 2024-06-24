from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cursos_matriculados = models.ManyToManyField('Curso', through='Matricula', related_name='alunos')

    def __str__(self):
        return f'Aluno: {self.nome} ({self.email})'

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidade = models.CharField(max_length=200)
    cursos = models.ManyToManyField('Curso', through='Alocacao', related_name='professores')

    def __str__(self):
        return f'Professor: {self.nome}, {self.especialidade}'

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    departamento = models.ForeignKey('Departamento', on_delete=models.CASCADE, related_name='cursos')
    salas = models.ManyToManyField('Sala', through='CursoSala')

    def __str__(self):
        return f'Curso: {self.nome} - {self.descricao}'

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    chefe = models.CharField(max_length=100)
    professores = models.ManyToManyField(Professor, related_name='departamentos')

    def __str__(self):
        return f'Departamento: {self.nome}, Chefe: {self.chefe}'

class Sala(models.Model):
    numero_sala = models.CharField(max_length=10)
    localizacao = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    cursos = models.ManyToManyField(Curso, through='CursoSala')

    def __str__(self):
        return f'Sala {self.numero_sala} - {self.localizacao}, Capacidade: {self.capacidade}'

class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField()

    def __str__(self):
        return f'Matrícula: Aluno {self.aluno.nome}, Curso {self.curso.nome}, Data {self.data_matricula}'

class Alocacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=20)

    def __str__(self):
        return f'Alocação: Professor {self.professor.nome}, Curso {self.curso.nome}, Semestre {self.semestre}'

class CursoSala(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario = models.CharField(max_length=20)

    def __str__(self):
        return f'Curso-Sala: Curso {self.curso.nome}, Sala {self.sala.numero_sala}, Horário {self.horario}'
