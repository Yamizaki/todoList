
from django.urls import path
from .views import showTasks, add, delete, done
urlpatterns = [
    path('', showTasks, name="showTasks"),
    path("add", add, name="add"),
    path("delete/<int:task_id>", delete, name="delete"),
    path("done/<int:task_id>", done, name="done")
]
