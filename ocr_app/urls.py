from django.urls import path, include
from . import views

urlpatterns = [
    path("list/", views.list, name="list"),
    path("", views.list)
]
# urlpatterns = patterns(
#     'myproject.myapp.views',
#     url(r'^list/$', 'list', name='list'),
# )