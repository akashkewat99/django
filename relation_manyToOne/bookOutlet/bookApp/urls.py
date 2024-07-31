from . import views
from django.urls import path

urlpatterns = [
    # path('',views.test,name="test"),
    path("", views.main, name="HomePage"),
    path('book/',views.books,name="bookHomePage"),
    path('author/',views.author,name="authorsHomePage"),
    # path('author/<int:id>/',views.authorDetail,name="authoeDetails"),
    path('author/<int:id>/',views.getSingleauthorDetail,name="authoeDetails"),
    path('book/<int:id>/',views.bookDetails,name="bookDetails"),


]