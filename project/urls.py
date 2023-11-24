"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from library.views import BookCreate,DeleteBook,EditBook,funcBooklist,funcBookDetail
from django.urls import path , include
#from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/',funcBooklist),
    #path('library/',BookList.as_view()),
    path('library/new',BookCreate.as_view()),
    path('library/<int:book_id>',funcBookDetail),
    #path('library/<int:pk>',BookDetail.as_view()),
    path('library/<int:pk>/edit/',EditBook.as_view),
    path('library/<int:pk>/delete/',DeleteBook.as_view),

]
