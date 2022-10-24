from django.urls import path
from app import views
from app.views import MyObtainTokenPairView, RegisterView,LogoutView, LogoutAllView,TicketsView,TicketsListView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [

      path('tickets/',TicketsView.as_view(),name='tickets'),
      path('tickets/<int:pk>/',TicketsListView.as_view(),name='ticketslist'),

      #login
      path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
      path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
      #register
      path('register/', RegisterView.as_view(), name='auth_register'),
      # path('<int:pk>/', views.ticket_view.as_view()),
      #logout
      path('logout/', LogoutView.as_view(), name='auth_logout'),
      path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),


]