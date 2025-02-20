from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from card.apps import CardConfig
from card.views import main, HistoryDetailView, ContactCreateView

from django.urls import path
from .views import main, HistoryDetailView

app_name = 'main'  # Убедитесь, что это определено

urlpatterns = [
    path("", main, name="main"),
    path('view/<int:pk>', HistoryDetailView.as_view(), name='view'),
]