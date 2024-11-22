from django.urls import path
from . import views
from .views import crop_fertilizer_prediction
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path("predict/", crop_fertilizer_prediction, name="predict"),
    path('fertilizers/', views.fertilizer_list, name='fertilizer_list'),
    path('fertilizers/<int:pk>/', views.fertilizer_detail, name='fertilizer_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

