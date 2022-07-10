from django.urls import path
from school_app.views import SchoolViewSet

urlpatterns = [
    path('', SchoolViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='school-list'),
    path('<int:pk>/', SchoolViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='school'),
    ]