from django.urls import path, include

from .views import RegisterUserApiView, StudentsApiView, StudentsViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('user_list', StudentsViewSet)

app_name = 'main'
urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterUserApiView.as_view(), name='register_user'),
    path('user_list/', StudentsApiView.as_view(), name='user_list'),
]