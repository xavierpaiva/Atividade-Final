from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'todos', views.TodoViewSet, basename='user-todos')
router.register(r'todos', views.TodoViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
]

urlpatterns += router.urls