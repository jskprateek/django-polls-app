from django.urls import path
from polls.views import IndexView, DetailView, ResultsView 
from . import views

app_name = 'polls'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('question/<int:pk>/', DetailView.as_view(), name='detail'),
    #path('<int:question_id>/', views.detail, name='detail'),
	path('<int:pk>/results/', ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]