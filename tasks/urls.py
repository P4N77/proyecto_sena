from django.urls import path, re_path
from . import views


app_name = 'tasks'

urlpatterns = [

    # añadir vegetal
    path('create/', views.task_create, name='task_create'),

    # detalles del vegetal añadido
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # actualizar vegetales
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),

    # eliminar vegetales
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

    # listar vegetales
    path('tasks/', views.task_list, name='task_list'),
    
    # inicio
    path('', views.index, name='index'),

    # salir / logout
    path('exit/',views.exit, name='salir'),

    # vista facturacion
    path('purchase/', views.task_purchase, name='purchase_vegetable'),
    
]