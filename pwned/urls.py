from django.urls import path
from . import views

urlpatterns = [
    path('pwned/<int:company_id>/', views.pwned_account, name='pwned_account'),

]