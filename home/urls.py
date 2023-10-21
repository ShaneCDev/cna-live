from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms-and-conditions', views.terms_and_cond, name='terms_and_cond'),
    path('privacy-policy', views.privacy_policy, name='privacy'),
]
