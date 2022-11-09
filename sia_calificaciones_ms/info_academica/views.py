
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Course, Grade, History
from .serializers import GradeSerializer, CourseSerializer, HistorySerializer
from rest_framework import serializers
from rest_framework import status
import logging
logger = logging.getLogger('django')

#ALL VIEW
@api_view(['GET'])
def all(request):
    api_urls = {
        'all_items': '/'
    }
@api_view(['GET'])
def listAll(request):
    # checking for the parameters from the URL
    grades = Grade.objects.all()
    course = Course.objects.all()
    history = History.objects.all()
    
    # if there is something in items else raise error
    if grades and course and history:
        serializerG = GradeSerializer(grades, many=True)
        serializerC = CourseSerializer(course, many=True)
        serializerH = HistorySerializer(history, many=True)

        return Response({'Histories': serializerH.data, 'Grades': serializerG.data, 'Courses': serializerC.data})

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

#GRADES VIEW
@api_view(['GET'])
def grades(request):
    api_urls = {
        'all_items': '/',
        'Search by Id': '/?id=grade_id',
        'Search by Course': '/?id_course=cour_id',
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
    courses = Course.objects.get(id=id_asig)
    serializer = CourseSerializer(courses)
    return serializer.data

#ASIGNATURES VIEW
@api_view(['GET'])
def courses(request):
    api_urls = {
        'all_items': '/',
        'Search by Id': '/?id=asig_id',
        'Search by Term': '/?term=term_val',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

@api_view(['GET'])
def listCourse(request):

    # checking for the parameters from the URL
    if request.query_params:
        course = Course.objects.filter(**request.query_params.dict())
    else:
        course = Course.objects.all()

    # if there is something in items else raise error
    if course:
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createCourse(request):
    course = CourseSerializer(data=request.data)
    
    if course.is_valid():
        course.save()
        return Response(course.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateCourse(request, pk):
    course = Course.objects.get(pk=pk)
    serializer = CourseSerializer(instance=course, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteCourse(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
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