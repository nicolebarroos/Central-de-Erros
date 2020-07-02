from django.urls import path

from .views import CadastroView
urlpatterns = [
    
    path('cadastro/', CadastroView.as_view()),
    #path('delete/<int:product_id>', views.delete_product, name='delete'),
    #path('update/<int:product_id>', views.update_product, name='update')
]