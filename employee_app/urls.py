from django.urls import path
from employee_app.views import EmployeeViewSet, PositionViewSet, DepartmentViewSet

urlpatterns = [
    path('', EmployeeViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='employee-list'),
    path('<int:pk>/', EmployeeViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'update', 'delete': 'destroy'}), name='employee-list'),

    path('position/', PositionViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='position-list'),
    path('position/<int:pk>/', PositionViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='position-list'),

    path('department/', DepartmentViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='department-list'),
    path('department/<int:pk>/', DepartmentViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='department-list'),
    ]


# CRUD
# C = create
# R = retrieve
# U = update
# D = destroy
