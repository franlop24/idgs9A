from django.shortcuts import render, HttpResponse, redirect
from books.models import Books, Users

# Create your views here.
def home(request):
    return render(request, 'books/home.html')



def prestamos(request):

    allUsers = Users.objects.filter(user_status = "1")

    return render(request, 'books/prestamos.html', {
        'user': allUsers
    })

def new_book(request):
    book = Books(
        title_book = 'Piense y hágase rico',
        author_book = 'Napoleón Hill',
        count_sale_book = '30 millones',
        image_book = 'piense_y_hagase_rico.jpg'
    )
    book.save()
    return redirect('../books/books')

def new_user(request):
    user = Users(
        user_name = 'Mariana',
        user_lastName = 'Vasquez',
        user_addres = 'Tlaxcala',
        user_celphone = '2474987125',
        reference_bookUser = '',
        user_status = False
    )
    user.save()
    return redirect('../books/clientes')

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

def find_book(request, name_book):
    
    findBook = Books.objects.filter(title_book = name_book)


    return render(request, 'books/book2.html',{
        'book': findBook
    })