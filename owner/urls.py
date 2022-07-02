from django.urls import path
from owner.views import ToLet, ToLetStatus

urlpatterns = [
    path('to/let/create/', ToLet.as_view()),
    path('to/let/update/', ToLet.as_view()),
    path('to/let/status/update/<str:id>/', ToLetStatus.as_view()),
    path('to/let/list/', ToLet.as_view()),
    path('to/let/delete/', ToLet.as_view()),
]
