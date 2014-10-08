# -*- coding: utf-8 -*-

#First, we import the class HttpResponse, which lives in the django.http module. We need to import this class because it’s used later in our code.

from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
	
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)	
# Next, we define a function called hello – the view function.

# Each view function takes at least one parameter, called request by convention. This is an object that contains information about the current Web request that has triggered this view, and it’s an instance of the class django.http.HttpRequest. In this example, we don’t do anything with request, but it must be the first parameter of the view nonetheless.

# Note that the name of the view function doesn’t matter; it doesn’t have to be named in a certain way in order for Django to recognize it. We’re calling it hello here, because that name clearly indicates the gist of the view, but it could just as well be named hello_wonderful_beautiful_world, or something equally revolting. The next section, “Your First URLconf”, will shed light on how Django finds this function.

# The function is a simple one-liner: it merely returns an HttpResponse object that has been instantiated with the text "Hello world".