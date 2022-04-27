from django.urls import path
from .views import ABC, DeleteCountry, DeleteState, GetAllCountry, GetCountryWiseState, InsertCountry, InsertState, UpdateCountry, UpdateState
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path('abc/', ABC.as_view(), name='abc'),

    #country api
    path('insert-country/', InsertCountry.as_view(), name='insert-country'),
    path('update-country/<int:id>', UpdateCountry.as_view(), name='update-country'),
    path('delete-country/<int:id>', DeleteCountry.as_view(), name='delete-country'),
    path('get-all-country/', GetAllCountry.as_view(), name='get-all-country'),

    #state api
    path('insert-state/', InsertState.as_view(), name='insert-state'),
    path('update-state/<int:id>', UpdateState.as_view(), name='update-state'),
    path('delete-state/<int:id>', DeleteState.as_view(), name='delete-state'),
    path('get-country-wise-state/<int:id>', GetCountryWiseState.as_view(), name='get-country0wise-state'),

  
]