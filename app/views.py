from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import simplejson
# Create your views here.

@csrf_exempt
def home(request):
	return render(request, 'index.html', {})



@csrf_exempt
def upload(request):
    try:
        if request.method == "POST":
            return HttpResponse(
                simplejson.dumps(
                    {"files": [
                      {
                        "name": "77464_537620316255351_1441662113_o.jpg",
                        "size": 902604,
                        "error": "Filetype not alloweddd"
                      }
                    ]}
                )
            )
    except:
        pass
    return render(request, 'home.html', {})