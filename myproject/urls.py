from django.contrib import admin
from django.urls import path

from authentication.views import LogoutView, SigninView, SignupView
from core.views import LatencyView
from users.views import InfoView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("signin/", SigninView.as_view(), name="signin"),
    path("info/", InfoView.as_view(), name="info"),
    path("latency/", LatencyView.as_view(), name="latency"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
