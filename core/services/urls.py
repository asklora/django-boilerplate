from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# URL patterns for ViewSets are added via rest_framework.routers.SimpleRouter
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'services'
urlpatterns = [
    path('', include(router.urls)),
    path('sample/', views.SampleAPI1.as_view())
]