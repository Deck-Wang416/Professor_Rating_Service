from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ModuleInstance
from .serializers import ModuleInstanceSerializer

class ModuleInstanceListView(APIView):
    def get(self, request):
        module_instances = ModuleInstance.objects.all()
        serializer = ModuleInstanceSerializer(module_instances, many=True)
        return Response(serializer.data)
