from django.shortcuts import render, redirect
from post.models import Post
# Create your views here.
# MVT - model veiw template

def index(request):
    cards = Post.objects.all()
    return render(request, 'index.html', {'cards':cards})



def about(request):
    return render(request, 'about.html')

def show_post(request, id):
    card = Post.objects.get(id=id)
    return render(request,'show_post.html', {'post':card})

def add_post(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    image = request.FILES.get('image')
    Post.objects.create(title=title, desciption=description, image=image, user_id=request.user)
    return redirect('home')
