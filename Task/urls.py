
from django.urls import path
from .views import showTasks, add, delete, done, pause, started, deleteAll
urlpatterns = [
    path('', showTasks, name="showTasks"),
    path("add", add, name="add"),
    path("deleteAll", deleteAll, name="deleteAll"),
    path("delete/<int:task_id>", delete, name="delete"),
    path("done/<int:task_id>", done, name="done"),
    path("pause/<int:task_id>", pause, name="pause"),
    path("started/<int:task_id>", started, name="started"),

]
