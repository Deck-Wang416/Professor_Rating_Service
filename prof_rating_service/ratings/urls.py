from django.urls import path
from .views import ModuleInstanceListView

urlpatterns = [
    path('modules/', ModuleInstanceListView.as_view(), name='module-list'),
]
