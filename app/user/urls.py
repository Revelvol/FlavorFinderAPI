
from django.urls import path
from . import views

app_name ='user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('update-me/', views.ManageUserView.as_view(), name='me'),
    path('token/', views.CreateTokenView.as_view(), name='token')
]
