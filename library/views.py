from django.shortcuts import render , redirect

# Create your views here.
from .models import Author,Book,Review
#from .form import BooksForm
#from .form import BooksForm



def funcBookDetail(request,book_id):
    data = Book.objects.get(id=book_id) # book_id is variable send to model Book to get specific row depend on id
    context ={
        'muhammed': data
    }
    return render(request,'library/book_detail.html',context)
    


def funcBooklist(request):
    data = Book.objects.all() #  
    context = {
        'ali':data
    }
    return render(request,'library/book_list.html',context)
    

def funCreateBook(request):
    if request.method == 'POST':
        form = BooksForm(request.POST)  # add ,request.FILE if data contain imeges or files
        if form.is_valid():
           # my = form.save(commit=False) # قبل ان تقوم بعملية الحفظ
           # my.author = request.user   # احفظ اسم المؤلف هو اسم المستخدم
            form.save()
            return redirect('/library/')
    else:
        form = BooksForm
    return render(request,'library/add_book.html',{'myform':form})



def funEditeBook(request,pk):
    data = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BooksForm(request.POST,instance=data)  # add ,request.FILE if data contain imeges or files
        if form.is_valid():
           # my = form.save(commit=False) # قبل ان تقوم بعملية الحفظ
           # my.author = request.user   # احفظ اسم المؤلف هو اسم المستخدم
            form.save()
            return redirect('/library/')
    else:
        form = BooksForm(instance=data)
    return render(request,'library/funEdit.html',{'myform':form})



def fundelete(request,pk):
    data = Book.objects.get(id=pk)
    data.delete()
    return redirect('/library/')

from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView

# class BookList(ListView):         # the name we use in the html file is the name of model_list or object_list
#     model = Book                  # the name of template or html  file is book_list


class BookDetail(DetailView):         # the name we use in the html file is the name of model or object
                                      # the name of template or html  file is book_detail
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