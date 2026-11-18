from django.urls import path
from .views import EndpointView

urlpatterns = [
    path('endpoint/', EndpointView.as_view()),
    path('endpoint/<int:id>/', EndpointView.as_view()),
]
