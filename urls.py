from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('', views.Home.as_view(), name='home'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
