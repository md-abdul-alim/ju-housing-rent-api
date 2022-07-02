from django.urls import path
from renter.views import CheckInAPI


urlpatterns = [
    path('check/in/list/', CheckInAPI.as_view()),
    path('check/in/create/', CheckInAPI.as_view()),
]