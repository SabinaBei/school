from django.urls import path
from students_app.views import StudentViewSet

urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='student-list'),
    path('<int:pk>/', StudentViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='student'),
    ]