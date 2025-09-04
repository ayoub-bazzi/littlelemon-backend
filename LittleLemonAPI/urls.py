from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegisterViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create DRF router
router = DefaultRouter()
router.register('menu-items', MenuItemViewSet, basename='menuitem')
router.register('bookings', BookingViewSet, basename='booking')
router.register('registration', RegisterViewSet, basename='registration')

# URL patterns for this app
urlpatterns = [
    path('', include(router.urls)),              # includes all viewsets
    path('api-token-auth/', obtain_auth_token),  # POST username/password -> token
]
