from rest_framework import serializers
from .models import ModuleInstance, Professor, Rating

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

class ProfessorWithRatingSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Professor
        fields = ['id', 'name', 'average_rating']

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(professor=obj)
        if ratings.exists():
            avg = sum(r.rating for r in ratings) / ratings.count()
            return round(avg)
        return None
