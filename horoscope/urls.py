from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='horoscope_index'),
    path('<int:sign_zodiac>', views.get_info_about_zodiac_sign_by_number),
    path('<str:sign_zodiac>', views.get_info_about_zodiac_sign, name='horoscope_name'),

]
