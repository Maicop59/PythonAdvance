from django.urls import path

from.import views
app_name="polls"

urlpatterns = [
    # /poll/
    path('', views.index, name = "index"),
    #/poll/5/
    path('<int:question_id>', views.detail, name = "detail"),
    #/poll/5/result
    path('<int:question_id>/result', views.result, name = "results"),
    path('<int:question_id>/vote', views.vote, name = "vote"),
    ]