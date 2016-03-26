from django.contrib import admin
from . models import Book, Review
# Register your models here.

#making book and review model entities modifiable in the admin site. 

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('book', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']

admin.site.register(Book)
admin.site.register(Review, ReviewAdmin)

