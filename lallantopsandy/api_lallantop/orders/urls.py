from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('orders' , views.orderView)

urlpatterns = [
    path('create' , views.createOrders.as_view()),
    path('edit' , views.editOrder.as_view()),
    path('' , include(router.urls))
]
