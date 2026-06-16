
from django.contrib import admin
from django.urls import path
from shop.views import index_page
urlpatterns = [
    path('',index_page),
    path('admin/', admin.site.urls),
]
