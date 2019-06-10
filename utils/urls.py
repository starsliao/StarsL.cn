from django.conf.urls import url
from .views import ip


urlpatterns = [
         url(r'^ip/$', ip.as_view()),
]
