from django.urls import path
from . import views

urlpatterns=[
    path("topping/", views.toppings, name="topping_all"),
    path("topping/add/", views.toppingCreate, name="topping_add"),
    path("topping/<str:id>/", views.toppingsEdit, name="topping_update_delete"),
    
    path("pizza/", views.pizzas, name="pizza_all"),
    path("pizza/add/", views.pizzaCreate, name="pizza_add"),
    path("pizza/<str:id>/", views.pizzasEdit, name="pizza_update_delete"),   
]