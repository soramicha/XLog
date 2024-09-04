from django.urls import path
from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("", views.register, name="register"),
    path("record", views.record, name="record"),
    path("monthly_summary", views.monthly_summary, name="monthly_summary"),
    path("yearly_summary", views.yearly_summary, name="yearly_summary")
]