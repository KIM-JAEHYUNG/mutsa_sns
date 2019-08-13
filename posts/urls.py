from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.show, name="show"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('<int:id>/new_comment/', views.new_comment, name="new_comment"),
    path('<int:id>/create_comment/', views.create_comment, name="create_comment"),
    path('<int:id>/like/', views.like, name="like"),
    path('favourite/', views.favourite, name="favourite"),

]