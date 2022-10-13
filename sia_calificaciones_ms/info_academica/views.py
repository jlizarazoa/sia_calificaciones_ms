
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Asignature, Grade, History
from .serializers import GradeSerializer, AsignatureSerializer, HistorySerializer
from rest_framework import serializers
from rest_framework import status
import logging
logger = logging.getLogger('django')

#GRADES VIEW
@api_view(['GET'])
def grades(request):
    api_urls = {
        'all_items': '/',
        'Search by Id': '/?id=grade_id',
        'Search by Asignature': '/?id_asignature=asig_id',
        'Add': '/create',
        'Update': '/update/ ',
        'Delete': '/item/pk/delete'
    }

@api_view(['GET'])
def listGrades(request):

    # checking for the parameters from the URL
    if request.query_params:
        grades = Grade.objects.filter(**request.query_params.dict())
        
    else:
        grades = Grade.objects.all()
    
    # if there is something in items else raise error
    if grades:
        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createGrades(request):
    grade = GradeSerializer(data=request.data)

    # validating for already existing data
    if Grade.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if grade.is_valid():
        grade.save()
        return Response(grade.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(grade.data)

@api_view(['PUT'])
def updateGrades(request, pk):
    grade = Grade.objects.get(pk=pk)
    serializer = GradeSerializer(instance=grade, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteGrades(request, pk):
    grade = Grade.objects.get(pk=pk)
    grade.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#Function to return asignature type
def retrieve(id_asig):
    asignature = Asignature.objects.get(id=id_asig)
    serializer = AsignatureSerializer(asignature)
    return serializer.data

#ASIGNATURES VIEW
@api_view(['GET'])
def asignatures(request):
    api_urls = {
        'all_items': '/',
        'Search by Id': '/?id=asig_id',
        'Search by Term': '/?term=term_val',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

@api_view(['GET'])
def listAsignature(request):

    # checking for the parameters from the URL
    if request.query_params:
        asignature = Asignature.objects.filter(**request.query_params.dict())
    else:
        asignature = Asignature.objects.all()

    # if there is something in items else raise error
    if asignature:
        serializer = AsignatureSerializer(asignature, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createAsignature(request):
    asignature = AsignatureSerializer(data=request.data)
    
    if asignature.is_valid():
        asignature.save()
        return Response(asignature.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateAsignature(request, pk):
    asignature = Asignature.objects.get(pk=pk)
    serializer = AsignatureSerializer(instance=asignature, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteAsignature(request, pk):
    asignature = Asignature.objects.get(pk=pk)
    asignature.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


#HISTORY VIEW
@api_view(['GET'])
def history(request):
    api_urls = {
        'all_items': '/',
        'Search by Id': '/?id=history_id',
        'Search by Program': '/?id_program=prog_id',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

@api_view(['GET'])
def listHistory(request):
 
    # checking for the parameters from the URL
    if request.query_params:
        history = History.objects.filter(**request.query_params.dict())
    else:
        history = History.objects.all()

    # if there is something in items else raise error
    if history:
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createHistory(request):
    history = HistorySerializer(data=request.data)
  
    # validating for already existing data
    if History.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if history.is_valid():
        history.save()
        return Response(history.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateHistory(request, pk):
    history = History.objects.get(pk=pk)
    serializer = HistorySerializer(instance=history, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteHistory(request, pk):
    history = History.objects.get(pk=pk)
    history.delete()
    return Response(status=status.HTTP_202_ACCEPTED)