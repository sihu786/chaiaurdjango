

from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('chai/',views.all_chai,name='all_chai'),
    path('<int:chai_id>/',views.chai_details,name='chai_details'),
    path('chai_store/',views.chai_store_view,name='chai_store'),
 

   
]
