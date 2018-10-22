from django.shortcuts import render

posts = [
    {
        'author':'person1',
        'title':'post 1',
        'content':'1st post content',
        'date_posted':'August 27, 2018'
    },
    {
        'author':'person2',
        'title':'post 2',
        'content':'2nd post content',
        'date_posted':'August 28, 2018'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
