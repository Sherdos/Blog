from django.shortcuts import render, HttpResponse

# Create your views here.
# MVT - model veiw template

cards = [
    {'title':'Hello','description':'ksdjpis'},
    {'title':'Hello2','description':'ksdjpis'},
    {'title':'Hello3','description':'ksdjpis'},
]

def index(request):
    
    return render(request, 'index.html', {'cards':cards})

def about(request):
    return render(request, 'about.html')