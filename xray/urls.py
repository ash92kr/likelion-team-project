from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.conf import settings


app_name='xray'

urlpatterns = [
    path('',views.XrayIndex.as_view(),name="index"),
    path('create/', views.XrayCreate.as_view(), name='create'),
    path('list/', views.XrayList.as_view(), name='list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
