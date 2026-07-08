from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalarySlipViewSet

router = DefaultRouter()
router.register('slips', SalarySlipViewSet)

urlpatterns = [path('', include(router.urls))]
