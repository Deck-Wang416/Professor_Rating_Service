from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ModuleInstance, Professor
from .serializers import ModuleInstanceSerializer, ProfessorWithRatingSerializer

class ModuleInstanceListView(APIView):
    def get(self, request):
        module_instances = ModuleInstance.objects.all()
        serializer = ModuleInstanceSerializer(module_instances, many=True)
        return Response(serializer.data)

class ProfessorListView(APIView):
    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorWithRatingSerializer(professors, many=True)
        return Response(serializer.data)
