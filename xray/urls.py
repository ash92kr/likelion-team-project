from django.urls import path
from . import views

app_name='xray'

urlpatterns = [
   path('',views.XrayIndex.as_view(),name="index"),
   
]