from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
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
        
class RateProfessorView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        professor_id = request.data.get('professor_id')
        module_code = request.data.get('module_code')
        year = request.data.get('year')
        semester = request.data.get('semester')
        rating_value = request.data.get('rating')

        if not (1 <= int(rating_value) <= 5):
            return Response({"error": "Rating must be between 1 and 5."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            professor = Professor.objects.get(id=professor_id)
        except Professor.DoesNotExist:
            return Response({"error": "Professor not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            module_instance = ModuleInstance.objects.get(
                module__code=module_code,
                year=year,
                semester=semester,
                professors=professor
            )
        except ModuleInstance.DoesNotExist:
            return Response({"error": "Module instance not found for given professor."}, status=status.HTTP_404_NOT_FOUND)

        Rating.objects.create(
            user=request.user,
            professor=professor,
            module_instance=module_instance,
            rating=rating_value
        )

        return Response({"message": "Rating submitted successfully!"}, status=status.HTTP_201_CREATED)
