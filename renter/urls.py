from django.urls import path
from renter.views import CheckInAPI, CheckOutAPI


urlpatterns = [
    path('check/in/', CheckInAPI.as_view()),
    path('check/in/list/', CheckInAPI.as_view()),
    path('check/in/update/<str:id>/', CheckInAPI.as_view()),
    path('check/out/', CheckOutAPI.as_view()),
    path('check/out/list/', CheckOutAPI.as_view()),
    path('check/out/update/<str:id>/', CheckOutAPI.as_view()),
]