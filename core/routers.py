from rest_framework import routers
from core.user.viewsets import UserViewSet

router = routers.SimpleRouter()

router.register(
    prefix=r'user', 
    viewset=UserViewSet, 
    basename='user'
    )

urlpatterns = [*router.urls,]