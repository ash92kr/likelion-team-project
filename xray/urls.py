from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings


app_name='xray'

urlpatterns = [
    path('',views.XrayIndex.as_view(),name="index"),
    path('create/', views.XrayCreate.as_view(), name='create'),
    path('list/', views.XrayList.as_view(), name='list'),
    path('<int:pk>/', views.XrayDetail.as_view(), name='detail'),
    path('<int:pk>/delete/', views.XrayDelete.as_view(), name='delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
