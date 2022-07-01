from django.shortcuts import render, HttpResponse, redirect
from books.models import Books, Users

# Create your views here.
def home(request):
    return render(request, 'books/home.html')



def prestamos(request):
    return render(request, 'books/prestamos.html')

def new_book(request):
    book = Books(
        title_book = 'Crepúsculo - La saga',
        author_book = 'Stephenie Meyer',
        count_sale_book = '43 millones',
        image_book = 'crepusculo_saga.jpg'
    )
    book.save()
    return redirect('../books/books')

def new_user():
    user = Users(
        user_name = 'Adrian',
        user_lastName = 'Garcia',
        user_addres = 'San Cosme',
        user_celphone = '2471055487',
        reference_bookUser = '',
        user_status = False
    )
    user.save()
    return redirect('../clientes')

def books(request):
    
    allBooks = Books.objects.all()

    return render(request, 'books/books.html',{
        'book': allBooks
    })

def users(request):

    allUsers = Users.objects.all()


    return render(request, 'books/clientes.html', {
        'user': allUsers
    })