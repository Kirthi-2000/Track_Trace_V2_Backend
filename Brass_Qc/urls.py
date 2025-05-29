from django.urls import path
from .views import *

urlpatterns = [
    path('brass_picktable/', BrassPickTableView.as_view(), name='BrassPickTableView'),
    path('iqf_picktable/', IqfPickTableView.as_view(), name='IqfPickTableView'),
    path('iqp_rejecttable/', IqpRejectTableView.as_view(), name='IqpRejectTableView'),


    path('R_brass_picktable/', R_BrassPickTableView.as_view(), name='R_BrassPickTableView'),
    path('R_iqf_picktable/', R_IqfPickTableView.as_view(), name='R_IqfPickTableView'),
    path('R_iqp_rejecttable/', R_IqpRejectTableView.as_view(), name='R_IqpRejectTableView'),
]