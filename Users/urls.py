from django.urls import path
from .views import SignupView, LoginView, NewsView, CRLAvailInstiView, CatAvailInstiView, TopBranchesYearWise, YearlyTrend, Branches, admin_only_view


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('news/', NewsView.as_view(), name='news'),
    path('crlavailinsti/', CRLAvailInstiView.as_view(), name='crlavailinsti'),
    path('catavailinsti/', CatAvailInstiView.as_view(), name='catavailinsti'),
    path('topbranchesyearwise/', TopBranchesYearWise.as_view(), name='topbranchesyearwise'),
    path('yearlytrend/', YearlyTrend.as_view(), name='yearlytrend'),
    path('branches/', Branches.as_view(), name='branches'),
    path('admin-view/', admin_only_view, name='admin-view'),
]
