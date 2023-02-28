from django.contrib import admin
from django.urls import path
import core.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.views.index, name='index'),
    path('result/', core.views.index, name='result')
]
