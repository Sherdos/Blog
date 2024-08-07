from django.shortcuts import render, redirect
from post.models import Like, Post, Comment, Review
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

def update_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        post.title = title
        post.desciption = description
        post.save()
        return redirect('show_post', post.id)
    return render(request, 'update_post.html',{'post':post})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')

def search_post(request):
    key = request.GET.get('key')
    cards = Post.objects.all()
    if key:
        cards = Post.objects.filter(title__icontains = key)
    return render(request, 'index.html'), {'cards':cards}

def add_comment(request, id):
    text = request.POST.get('text')
    Comment.objects.create(text = text, user = request.user, post_id = id)
    return redirect('show_post', id)

def like(request, id):
    try:
        like_post = Like.objects.get( user = request.user, post_id = id)
        like_post.delete()
    except:
        Like.objects.create( user = request.user, post_id = id)
    return redirect('show_post', id)

def add_review(request):
    text = request.POST.get('text')
    Review.objects.create(text=text, user=request.user)
    return redirect('home')
