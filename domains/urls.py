from django.urls import path
from . import views

urlpatterns = [
    path('similar_domains/<int:company_id>/', views.domains, name='domains'),

]