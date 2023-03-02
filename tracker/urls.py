from django.urls import path
from tracker.views.index import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
]