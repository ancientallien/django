
from django.contrib import admin
from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ResumePageView
from .views import PortfolioPageView
from .views import ContactPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about", AboutPageView.as_view(), name="about"),
    path("resume", ResumePageView.as_view(), name="resume"),
    path("portfolio", PortfolioPageView.as_view(), name="portfolio"),
    path("contact", ContactPageView.as_view(), name="contact"),
]


