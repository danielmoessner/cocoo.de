from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('imagefit/', include('imagefit.urls')),
    path('team/', views.MemberListView.as_view(), name='member_list'),
    path('kontakt/', views.ContactView.as_view(), name='contact'),
    path('impressum/', views.ImprintView.as_view(), name='imprint'),
    path('datenschutz/', views.DateProtectionView.as_view(), name='data_protection'),
    path('seminargruppen/', views.SeminarGroupListView.as_view(), name='seminargroup_list'),
    # remove maybe
    path('seminargruppe/<slug:slug>/', views.SeminarGroupDetailView.as_view(), name='seminargroup_detail'),
    # end remove
    path('seminarthema/<slug:slug>/', views.SeminarTopicDetailView.as_view(), name='seminartopic_detail'),
    path('team/<slug:slug>/', views.MemberDetailView.as_view(), name='member_detail'),
]
