from django.urls import path
from . import views 

urlpatterns = [
    path('submit/', views.submit_slip, name='submit_slip'),
    path('results/<int:slip_id>/', views.slip_results, name='slip_results'),
]