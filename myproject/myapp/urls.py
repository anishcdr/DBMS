    # myapp/urls.py
from django.urls import path
from . import views
from .views import ReceiveDataFromRoverAPIView


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('npk/', views.grid_section_detail, name='npk'),
    path('water/', views.moisture, name='water'),
    path('ranking/', views.ranking, name='ranking'),
    path('fixture_filter/',views.fixture_filter,name='fixture'),
    path('result_filter/',views.result_filter,name='result'),
    path('ranking_filter/',views.ranking_filter,name='ranking_filter'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('download_csv1/', views.download_csv1, name='download_csv1'),
    path('download_csv2/', views.download_csv2, name='download_csv2'),
    #path('receive_data_from_rover/', views.receive_data_from_rover, name='receive_data_from_rover'),
    path('receive_data_from_rover/', ReceiveDataFromRoverAPIView.as_view(), name='receive_data_from_rover'),
]
