from django.conf.urls import url,include
from portfolio import views

urlpatterns = [
    url(r'index/',views.index,name='index'),
]
