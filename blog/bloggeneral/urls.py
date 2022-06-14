from django.urls import path
from bloggeneral import views


urlpatterns = [
    path('',views.home ),
    path('crear/',views.CrearBlog ),
    path('modificar/',views.ModificarBlog ),
    path('eliminar/',views.EliminarBlog ),
]
