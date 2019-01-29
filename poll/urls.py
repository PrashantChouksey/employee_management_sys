from django.urls import path, include
from poll.views import *
urlpatterns = [
    path('', index, name="index"),
    path('<int:id>/details', details, name="details"),
    path('<int:id>/', poll, name="single_poll"),
    path('<int:id>/delete', poll_delete, name="poll_delete"),
    path('add/', PollView.as_view() , name="poll_add"),
    path('<int:id>/edit', PollView.as_view() , name="poll_edit"),
]
