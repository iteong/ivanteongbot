# ivanteongbot/fb_ivanteongbot/urls.py
from django.conf.urls import include, url # add this
from .views import IvanTeongBotView
urlpatterns = [
				url(r'^99789126bd00b5454d999cf3a9c3f8a9274d4e1460ac4b9863/?$', IvanTeongBotView.as_view()) 
			  ]
