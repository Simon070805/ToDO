from django.urls import path

from apps.users.views import UserAPIViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserAPIViewSet,basename="user_api" )

urlpatterns = [

]
urlpatterns += router.urls
