from django.urls import path
from . import views


urlpatterns = [
    path('', views.All, name='home'),
    path('all/', views.listAll, name='view-all'),
    path('g', views.grades, name='home-grades'),
    path('grades/', views.listGrades, name='view-grades'),
    path('grades/create', views.createGrades, name='add-grades'),
    path('grades/update/<int:pk>', views.updateGrades, name='update-grades'),
    path('grades/<int:pk>/delete', views.deleteGrades, name='delete-grades'),
    path('a', views.courses, name='homeCourses'),
    path('courses/', views.listCourse, name='view-courses'),
    path('courses/create', views.createCourse, name='add-courses'),
    path('courses/update/<int:pk>', views.updateCourse, name='update-courses'),
    path('courses/<int:pk>/delete', views.deleteCourse, name='delete-courses'),
    path('h', views.history, name='homeHistory'),
    path('history/', views.listHistory, name='view_history'),
    path('history/create', views.createHistory, name='add-history'),
    path('history/update/<int:pk>', views.updateHistory, name='update-history'),
    path('history/<int:pk>/delete', views.deleteHistory , name='delete-history'),
]