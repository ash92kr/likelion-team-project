from django.urls import path#, include
from . import views

app_name = 'book'

urlpatterns = [
    path('',views.BookIndex.as_view(),name='index'),
    # path('admin/', admin.site.urls),
    # path('accounts/',include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('xray/',include('xray.urls')),

]


