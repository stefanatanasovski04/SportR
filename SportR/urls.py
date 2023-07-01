"""
URL configuration for SportR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from eshop import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('sneakers/', views.sneakers, name="sneakers"),
    path('go_to_detailed_view/', views.go_to_detailed_view, name="go_to_detailed_view"),
    path('detailedView/', views.detailedView, name="detailedView"),
    path('update_item/', views.update_item, name='update_item'),
    path('delete_item/', views.delete_item, name='delete_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('order_successful', views.order_confirmation, name='order_confirmation'),
    path('get_add_product/', views.get_add_product, name='get_add_product'),
    path('confirmation_for_product/', views.successfully_added, name='confirmation_for_product'),

    # path('delete/', views.delete,name='delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
