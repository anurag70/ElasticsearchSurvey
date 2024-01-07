from django.urls import path
from compensation_logs.views import *

urlpatterns = [
    path('upload/s1/', UploadCompensationDataViewS1.as_view(), name='upload'),
    path('upload/s2/', UploadCompensationDataViewS2.as_view(), name='upload'),
    path('compensation_data/', CompensationDataViewSet.as_view(), name='compensation_data_list'),
    path('compensation_data/get_data_by_id/', CompensationDataViewSetById.as_view(), name='compensation_data_by_id'),
    path('compensation_data/get_data_by_fields/', CompensationDataViewSetByFields.as_view(), name='compensation_data_by_fields'),
]