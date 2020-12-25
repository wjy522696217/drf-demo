from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
