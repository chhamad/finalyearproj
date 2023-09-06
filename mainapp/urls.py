# mainapp/urls.py

from django.urls import path
from .views import home, register,login, edit_profile, handle_case, dashboard,review, profile, chat_view,agreement,lawyer

urlpatterns = [
    path('', home.home, name='home'),
    path('register/', register.register_user, name='register'),
    path('login/', login.login_user, name='login'),
    path('logout/', login.logout_user, name='logout'),
    path('edit_profile/', edit_profile.edit_profile, name='edit_profile'),
    path('handle_case/', handle_case.handle_case, name='handle_case'),
    path('leave_review/<int:lawyer_id>/', review.leave_review, name='leave_review'),
    path('my_lawyer', lawyer.my_lawyer, name='my_lawyer'),
    path('create_hiring/<int:lawyer_id>/', lawyer.create_hiring, name='create_hiring'),
    path('delete_hiring/<int:lawyer_id>/', lawyer.delete_hiring, name='delete_hiring'),
    path('dashboard/', dashboard.client_dashboard, name='client_dashboard'),
    path('search/', lawyer.search_lawyers, name='search_lawyers'),
    path('profile/<int:lawyer_id>/', profile.view_profile, name='view_profile'),
    path('my-profile/', profile.my_profile, name='my_profile'), 
    path('chat_view/', chat_view.chat_view, name= "chat_view"),
    path('friend/<str:pk>', chat_view.chat_detail, name="chat_detail"),
    path('sent_msg/<str:pk>', chat_view.sentMessages, name = "sent_msg"),
    path('rec_msg/<str:pk>', chat_view.receivedMessages, name = "rec_msg"),
    path('notification', chat_view.chatNotification, name = "notification"),
    path('terms-of-service/', agreement.terms_of_service, name='terms_of_service'),
    path('user-agreement/', agreement.user_agreement, name='user_agreement'),
    path('cases/', dashboard.cases, name='cases'),
    path('lawyer_cases/', dashboard.lawyer_cases, name='lawyer_cases'),
    path('filter_lawyers/', dashboard.filter_lawyers, name='filter_lawyers'),



]
