from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from .models import Aluno, Professor, Curso
from .serializers import AlunoSerializer, ProfessorSerializer, CursoSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def aluno_list(request):
    if request.method == 'GET':
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def aluno_detail(request, pk):
    try:
        aluno = Aluno.objects.get(pk=pk)
    except Aluno.DoesNotExist:
        return Response({'status': 'ERRO', 'mensagem': 'Aluno não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AlunoSerializer(aluno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            aluno.delete()
            return Response({'status': 'SUCESSO', 'mensagem': 'Aluno deletado com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'ERRO', 'mensagem': f'Erro ao deletar aluno: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def aluno_search(request):
    query = request.query_params.get('q', None)
    alunos = Aluno.objects.filter(Q(nome__icontains=query) | Q(matricula__icontains=query))
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def professor_list(request):
    if request.method == 'GET':
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def professor_detail(request, pk):
    try:
        professor = Professor.objects.get(pk=pk)
    except Professor.DoesNotExist:
        return Response({'status': 'ERRO', 'mensagem': 'Professor não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfessorSerializer(professor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            professor.delete()
            return Response({'status': 'SUCESSO', 'mensagem': 'Professor deletado com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'ERRO', 'mensagem': f'Erro ao deletar professor: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professor_search(request):
    query = request.query_params.get('q', None)
    professores = Professor.objects.filter(Q(nome__icontains=query) | Q(departamento__icontains=query))
    serializer = ProfessorSerializer(professores, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def curso_list(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def curso_detail(request, pk):
    try:
        curso = Curso.objects.get(pk=pk)
    except Curso.DoesNotExist:
        return Response({'status': 'ERRO', 'mensagem': 'Curso não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CursoSerializer(curso)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        try:
            curso.delete()
            return Response({'status': 'SUCESSO', 'mensagem': 'Curso deletado com sucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'ERRO', 'mensagem': f'Erro ao deletar curso: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def curso_search(request):
    query = request.query_params.get('q', None)
    cursos = Curso.objects.filter(Q(nome__icontains=query) | Q(codigo__icontains=query))
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def aluno_matriculas(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    cursos = aluno.curso_set.all()
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def professor_cursos(request, pk):
    professor = Professor.objects.get(pk=pk)
    cursos = professor.curso_set.all()
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def curso_alunos(request, pk):
    curso = Curso.objects.get(pk=pk)
    alunos = curso.aluno_set.all()
    serializer = AlunoSerializer(alunos, many=True)
    return Response(serializer.data)
