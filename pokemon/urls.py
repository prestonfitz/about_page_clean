from django.urls import path
from .views import indexPageView
from .views import authorPageView
from .views import ballsPageView
from .views import startersPageView
from .views import typesPageView

app_name = 'pokemon'
urlpatterns = [
    path("", indexPageView, name="index"),
    path("author/", authorPageView, name="author"),
    path("pokeballs/", ballsPageView, name="pokeballs"),
    path("starters/", startersPageView, name="starters"),
    path("types/", typesPageView, name="types"),
]
