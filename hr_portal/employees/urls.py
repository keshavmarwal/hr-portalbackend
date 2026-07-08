from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet

router = DefaultRouter()
router.register('list', EmployeeViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = [path('', include(router.urls))]
