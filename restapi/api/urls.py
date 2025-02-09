from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.blood_test_detail, name='blood_test_detail'),
    path('blood-tests/', views.BloodTestList.as_view()),
    path('blood-tests/<int:pk>/', views.BloodTestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
