from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.bloggirls),		# r expresion regular			$ solo directorio raiz
    

]