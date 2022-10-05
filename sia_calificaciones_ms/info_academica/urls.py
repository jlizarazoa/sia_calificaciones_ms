from django.urls import path
from . import views


urlpatterns = [
    path('g', views.grades, name='homeGrades'),
    path('grades/', views.listGrades, name='view-grades'),
    path('grades/create', views.createGrades, name='add-grades'),
    path('grades/update/<int:pk>', views.updateGrades, name='update-grades'),
    path('grades/<int:pk>/delete', views.deleteGrades, name='delete-grades'),
    path('a', views.asignatures, name='homeAsignatures'),
    path('asignatures/', views.listAsignature, name='view_asignatures'),
    path('asignatures/create', views.createAsignature, name='add-asignatures'),
    path('asignatures/update/<int:pk>', views.updateAsignature, name='update-asignatures'),
    path('asignatures/<int:pk>/delete', views.deleteAsignature, name='delete-asignatures'),
    path('h', views.history, name='homeHistory'),
    path('history/', views.listHistory, name='view_history'),
    path('history/create', views.createHistory, name='add-history'),
    path('history/update/<int:pk>', views.updateHistory, name='update-history'),
    path('history/<int:pk>/delete', views.deleteHistory , name='delete-history'),
]