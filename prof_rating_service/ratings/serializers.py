from rest_framework import serializers
from .models import ModuleInstance, Professor

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id', 'name']

class ModuleInstanceSerializer(serializers.ModelSerializer):
    professors = ProfessorSerializer(many=True, read_only=True)
    module_name = serializers.CharField(source='module.name')
    module_code = serializers.CharField(source='module.code')

    class Meta:
        model = ModuleInstance
        fields = ['module_code', 'module_name', 'year', 'semester', 'professors']
