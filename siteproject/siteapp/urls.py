from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.contact,name='contact'),
    # path('op/',views.operation,name='operation'),
]