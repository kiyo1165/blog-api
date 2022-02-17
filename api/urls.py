from django.urls import path, include
from .views import TaskListView, TaskRetrieveView, TaskViewSet, CreateUserView, PostRetrieveView, PostListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', TaskViewSet, basename="task")

urlpatterns = [
    path('list-task/', TaskListView.as_view(), name="list-task" ),
    path('detail-task/<str:pk>/', TaskRetrieveView.as_view(), name="detail-task" ),
    path('detail-post/<str:pk>/', PostRetrieveView.as_view(), name="detail-post" ),
    path('list-post/', PostListView.as_view(), name="list-post" ),
    path('register/', CreateUserView.as_view(), name="register" ),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
