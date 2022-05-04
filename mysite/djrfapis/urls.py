from django.urls import path, reverse_lazy, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name='apis'
urlpatterns = [
    path('', views.TestView.as_view(), name='apis'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', obtain_auth_token, name="obtain")
]