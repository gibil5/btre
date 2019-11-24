"""

Views - Listing

Created: 24 Nov 2019
Last up: 24 Nov 2019
"""

from django.shortcuts import render

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .models import Listing


# Create your views here.

def index(request):
	print()
	print('index')

	#objs = Listing.objects.all()
	objs = Listing.objects.order_by('-list_date').filter(is_published=True)

	paginator = Paginator(objs, 6)

	page = request.GET.get('page')

	paged_objs = paginator.get_page(page)

	ctx = {
		#'objs': objs,
		'objs': paged_objs,
	}
	
	return render(request, 'listings/listings.html', ctx)


def listing(request, listing_id):
	return render(request, 'listings/listing.html')


def search(request):
	return render(request, 'listings/search.html')
