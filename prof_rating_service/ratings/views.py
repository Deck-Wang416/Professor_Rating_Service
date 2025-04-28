from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ModuleInstance, Professor, Module, Rating
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

class ProfessorModuleAverageRatingView(APIView):
    def get(self, request, professor_id, module_code):
        try:
            module = Module.objects.get(code=module_code)
        except Module.DoesNotExist:
            return Response({"error": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
        
        ratings = Rating.objects.filter(
            professor__id=professor_id,
            module_instance__module=module
        )

        if ratings.exists():
            avg = sum(r.rating for r in ratings) / ratings.count()
            avg = round(avg)
            return Response({
                "professor_id": professor_id,
                "module_code": module_code,
                "average_rating": avg
            })
        else:
            return Response({
                "professor_id": professor_id,
                "module_code": module_code,
                "average_rating": None
            })
