from django import forms
from .models import Book

class BooksForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__' # هنا اذا اردنا ان نظهر جميع الحقول
        #fields = ['title','content','draft','publish_date','image','category'] # هنا اذا اردنا ان نظهر حقول معينة
        #exclude = ('auther',) # هنا اذا اردنا ان نستثني اظهار حقول معينة للمستخدم