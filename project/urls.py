from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [
    path('',views.book_list,name="home_page"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)