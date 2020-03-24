from django.urls import path
from .views import Index, Edit,PostDetail

urlpatterns = [
    path('',Index.as_view(), name='get'),
    path('post/new/',Edit.as_view(),name='get'),
    path('post/new/',Edit.as_view(), name='post'),
    path('post_detail/<int:pk>/',PostDetail.as_view(), name='get'),
]