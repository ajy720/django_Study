from django.urls import path
from lovely.views import first, second, third


app_name = "lovely"
urlpatterns = [
    path("first/", first, name="first"),
    path("second/", second, name="second"),
    path("third/", third, name="third"),
]
