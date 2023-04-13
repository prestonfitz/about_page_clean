from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import contactPageView
from .views import resumePageView
from .views import tableauPageView

app_name = 'aboutMe'
urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    path("resume/", resumePageView, name="resume"),
    path("tableau/", tableauPageView, name="tableau"),
]
