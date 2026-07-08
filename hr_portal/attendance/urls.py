from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, LeaveRequestViewSet

router = DefaultRouter()
router.register('records', AttendanceViewSet)
router.register('leaves', LeaveRequestViewSet)

urlpatterns = [path('', include(router.urls))]
