from django.urls import path, reverse_lazy, include
from . import views

app_name='apis'
urlpatterns = [
    path('', views.TestView.as_view(), name='apis'),
    path('api-auth/', include('rest_framework.urls'))
]