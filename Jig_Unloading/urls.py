from django.urls import path
from .views import *

urlpatterns = [
    path('JigUnloading_Completedtable/', JigUnloading_Completedtable.as_view(), name='JigUnloading_Completedtable'),
    path('Jig_Unloading_Main/', Jig_Unloading_Main.as_view(), name='Jig_Unloading_Main'),
    # Nickel Maintable URL
    path('Nickel_Maintable/', Nickel_Maintable.as_view(), name='Nickel_Maintable'),
]