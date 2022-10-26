
from turtle import home
from django.contrib import admin
from django.urls import path
from django.views import View
from smartphone_app.views import (

    get_all_company,
    get_company_by_name,
    Homeview

         

    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', get_all_company),
    path('company/<str:company>/', get_company_by_name, name='company'),
    path('', Homeview.as_view()),
]