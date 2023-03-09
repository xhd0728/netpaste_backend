from django.urls import path
from . import views

urlpatterns = {
    path("text", views.TextView.as_view()),
    path("texts", views.TextViews.as_view()),
}
