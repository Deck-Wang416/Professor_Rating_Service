from django.urls import path
from .views import ModuleInstanceListView, ProfessorListView, ProfessorModuleAverageRatingView, RateProfessorView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('modules/', ModuleInstanceListView.as_view(), name='module-list'),
    path('professors/', ProfessorListView.as_view(), name='professor-list'),
    path('professors/<str:professor_id>/module/<str:module_code>/average/', ProfessorModuleAverageRatingView.as_view(), name='professor-module-average'),
    path('rate/', RateProfessorView.as_view(), name='rate-professor'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
