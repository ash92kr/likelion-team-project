<<<<<<< HEAD
from django.urls import path#, include
=======
from django.urls import path
>>>>>>> 56fa93dd07585789d29e76febb97773c067020d0
from . import views

app_name = 'book'

urlpatterns = [
<<<<<<< HEAD
    path('',views.BookIndex.as_view(),name='index'),
    # path('admin/', admin.site.urls),
    # path('accounts/',include('accounts.urls')),
    # path('accounts/', include('allauth.urls')),
    # path('xray/',include('xray.urls')),

=======
   path('',views.BookIndex.as_view(),name='index'),
   
>>>>>>> 56fa93dd07585789d29e76febb97773c067020d0
]


