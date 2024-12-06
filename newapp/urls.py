from django.urls import path
from newapp.apps import NewappConfig
from newapp.views import home


app_name = NewappConfig.name


urlpatterns = [
    path('', home, name='index')
]
