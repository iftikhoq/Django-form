from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="homepage"),
    path('feedbackform/', views.feedbackform, name="feedbackForm"),
    path('admin/', admin.site.urls),
]
