from django.urls import path
from owner.views import ToLet, ToLetStatus, CheckInAcceptReject

urlpatterns = [
    path('to/let/create/', ToLet.as_view()),
    path('to/let/update/', ToLet.as_view()),
    path('to/let/status/update/<str:id>/', ToLetStatus.as_view()),
    path('to/let/list/', ToLet.as_view()),
    path('to/let/delete/', ToLet.as_view()),
    path('check/accept/<str:id>/', CheckInAcceptReject.as_view()),
    path('check/reject/', CheckInAcceptReject.as_view()),

]
