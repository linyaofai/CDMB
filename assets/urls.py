from assets import views
from django.urls import path
app_name = 'assets'

urlpatterns = [
    path('report/', views.report, name='report'),
]