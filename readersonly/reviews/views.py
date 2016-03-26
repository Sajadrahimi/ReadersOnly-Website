from django.shortcuts import get_object_or_404, render

from .models import Review, Book

# Create your views here.
#views with different url mappings


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def book_list(request):
    book_list = Book.objects.order_by('-name')
    context = {'book_list':book_list}
    return render(request, 'reviews/book_list.html', context)


def book_detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'reviews/book_detail.html', {'book':book})