from django.urls import path, include
from poll import views


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('polls/', views.PollListView.as_view()),
    path('polls/<int:pk>/', views.PolDetailView.as_view()),
    path('questions/', views.QuestionListView.as_view()),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view()),
    path('variants/', views.AnswerVariantListView.as_view()),
    path('answers/', views.PollParticipationView.as_view()),
    path('answers/<int:participant_id>/', views.PollParticipationDetailsView.as_view()),
]
