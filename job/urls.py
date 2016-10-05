from job import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'index/', views.index, name='index', ),
    url(r'addjob/', views.addJob, name="add_job"),
]
