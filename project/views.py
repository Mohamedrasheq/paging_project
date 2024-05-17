# views.py
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book



def book_list(request):
    book_queryset = Book.objects.all()  # Get all books
    paginator = Paginator(book_queryset, 5)  # 10 books per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the specific page

    context = {
        'page_obj': page_obj,
    }

    return render(request, 'book_list.html', context)


