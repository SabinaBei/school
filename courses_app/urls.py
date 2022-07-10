from django.urls import path
from courses_app.views import CourseViewSet

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='course-list'),
    path('<int:pk>/', CourseViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='course-list'),
]
