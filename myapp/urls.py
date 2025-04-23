from django.urls import path
from . import views


app_name= 'myapp'


urlpatterns = [
    path('',views.index),
    path('<int:my_id>/',views.current_index, name='detail'),
    
]
