from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name="about.html")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('level1/', include('level1.urls')),
]