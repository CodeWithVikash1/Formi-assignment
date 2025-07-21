from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('classify-query/', views.classify_query, name='classify-query'),
    path('retrieve-info/', views.retrieve_info, name='retrieve-info'),
]
