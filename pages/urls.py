from django.urls import path, include
from django.views.generic import TemplateView

from .views import form

app_name = 'pages'

urlpatterns = [
    # path('', TemplateView.as_view(template_name='pages/index.html'), name='home'),
    path('', form, name='home'),
    path('plug/', TemplateView.as_view(template_name='pages/plug.html'), name='plug'),

]
