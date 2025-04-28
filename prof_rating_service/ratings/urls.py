from django.urls import path
from .views import ModuleInstanceListView, ProfessorListView

urlpatterns = [
    path('modules/', ModuleInstanceListView.as_view(), name='module-list'),
    path('professors/', ProfessorListView.as_view(), name='professor-list'),
]
