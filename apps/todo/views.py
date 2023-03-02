from rest_framework.viewsets import GenericViewSet, mixins

from apps.todo.models import Task
from apps.todo.serializers import TaskSerializer

# Create your views here.
class TodoAPIViewSet(GenericViewSet,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

