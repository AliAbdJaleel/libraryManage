from django.shortcuts import render

# Create your views here.
from .models import Author,Book,Review

#from .form import BooksForm



def funcBookDetail():
    pass


def funcBooklist(request):
    data = Book.objects.all()  
    context = {
        'ali':data
    }
    return render(request,'library/book_list.html',context)
    


from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView

class BookList(ListView):
    model = Book


class BookDetail(DetailView):
    model = Book




class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/library/'

class EditBook(UpdateView):
    model = Book
    fields = '__all__'
    success_url = '/library/'
    template_name = 'library/edit.html'

class DeleteBook(DeleteView):
    model = Book
    success_url = '/library/'