from django.urls import path
from . import views

urlpatterns = [
    path('detail',views.detail),
    path('detail2',views.detail2 , name="detail_list")
]
