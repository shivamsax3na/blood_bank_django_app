from django.urls import path
# from . import views
from .views import HomeListView, DonerDetailView, HomeListView, DonerRequest, UpdatePostView, DeletePostView

urlpatterns = [
	path('', HomeListView.as_view(), name="home"),
	path('doner/<int:pk>', DonerDetailView.as_view(), name="DonerDetailView"),
	path('donaterequest/', DonerRequest.as_view(), name="DonerRequest"),
	path('donaterequest/edit/<int:pk>', UpdatePostView.as_view(), name="UpdatePost"),
	path('donaterequest/edit/<int:pk>/remove', DeletePostView.as_view(), name="DeletePost"),

]

