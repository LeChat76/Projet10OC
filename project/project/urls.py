from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from authentication.views import UserViewset
from softdesk.views import ContributorViewset, ProjectViewset, IssueViewset, CommentViewset, ProjectIssueViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register('user', UserViewset, basename='user')
router.register('contributor', ContributorViewset, basename='contributor')
router.register('project', ProjectViewset, basename='project')
router.register('project/(?P<project_pk>\d+)/issue', ProjectIssueViewset, basename='project_issue')
router.register('issue', IssueViewset, basename='issue')
router.register('comment', CommentViewset, basename='comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/project/<int:pk>/issue/', ProjectIssueViewset.as_view(), name='project_issue'),
]
