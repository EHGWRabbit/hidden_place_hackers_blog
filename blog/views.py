from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator 
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger 
from django.views.generic import ListView 
from .forms import EmailPostForm 
from django.core.mail import send_mail 


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name= 'posts'#context variable 
    paginate_by = 4#defferent result for 4 objects on page
    template_name = 'blog/list.html'
def post_list(request):
    object_list = Post.published.all()#create exemple from clsss Paginator
    paginator = Paginator(object_list, 4)#count objects for page 
    page = request.GET.get('page')#this number page 
    try:
        posts = paginator.page(page)#method 'page' from class Paginator 
    except PageNotAnInteger:
        posts = paginator.page(1)#if page not whole number get 1 page 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)#send number page and renreding template 
    return render(request, 'blog/list.html', {'page': page, 'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', 
    publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/detail.html', {'post': post})

def post_share(request, post_id):#create view 
    post = get_object_or_404(Post, id=post_id, status='published')#get ,message from his id 
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)#form sent 
        if form.is_valid():#fields is norm 
            cd = form.cleaned_data#email send 
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) рекомендуем прочитать "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Читать "{}" в {}\n\n{}\' комментарии: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myhiddenblog.com', [cd['to']])
            sent = True
    else:#in negative 
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post': post, 'form': form, 'sent': sent})

