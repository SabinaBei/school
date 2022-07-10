from django.urls import path
from employee_app.views import EmployeeViewSet, PositionViewSet, DepartmentViewSet

urlpatterns = [
    path('', EmployeeViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='employee-list'),
    path('<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'}), name='employee-list'),

    path('', PositionViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='position-list'),
    path('<int:pk>/', PositionViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='position-list'),

    path('', DepartmentViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='department-list'),
    path('<int:pk>/', DepartmentViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='department-list'),
    ]