from django.urls import path
from bloggeneral import views


urlpatterns = [
    path('',views.home.as_view(), name='home'),
    path('crear/',views.crearBlog.as_view(), name='crear'),
    path('modificar/',views.ModificarBlog, name='editar'),
    path('eliminar/', views.EliminarBlog.as_view(), name='eliminar'),
]
