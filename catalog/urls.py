from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home, contacts


app_name = NewappConfig.name


urlpatterns = [
    path('home/', home, name='index'),
    path('contacts/', contacts, name='contacts')
]
