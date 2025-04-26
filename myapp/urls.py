from django.urls import path
from . import views


app_name= 'myapp'


urlpatterns = [
    path('',views.index,name='index'),
    path('<int:my_id>/',views.current_index, name='detail'),
    path('additem/', views.add_item, name="additem"),
    path('updateitem/<int:my_id>/', views.update_item, name="update_item"),
    path('deleteitem/<int:my_id>/', views.delete_item, name="delete_item"),
    
]
