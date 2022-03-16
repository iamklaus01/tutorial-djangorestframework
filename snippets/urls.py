from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

#Here we create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

#This part of code will be uncommented if we don't want to use routers
''' from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('snippets/', SnippetList ,  name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetail , name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', SnippetHighlight , name='snippet-highlight'),
    path('users/', UserList , name='user-list'),
    path('users/<int:pk>/', UserDetail , name='user-detail')
]) '''