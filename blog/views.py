from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator 
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger 
from django.views.generic import ListView 
from .forms import EmailPostForm 
from django.core.mail import send_mail 
from .models import Comment 
from .forms import CommentForm 
from taggit.models import Tag 
from django.db.models import Count 



'''
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name= 'posts'#context variable 
    paginate_by = 4#defferent result for 4 objects on page
    template_name = 'blog/list.html'
'''
def post_list(request, tag_slug=None):
    object_list = Post.published.all()#create exemple from clsss Paginator
    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 4)#count objects for page 
    page = request.GET.get('page')#this number page 
    try:
        posts = paginator.page(page)#method 'page' from class Paginator 
    except PageNotAnInteger:
        posts = paginator.page(1)#if page not whole number get 1 page 
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)#send number page and renreding template 
    return render(request, 'blog/list.html', {'page': page, 'posts': posts, 'tag': tag})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', 
    publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)#list active comment this post 
    new_comment = None 
    if request.method == 'POST':#comment sent 
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)#create object comment but not save 
            new_comment.post = post#net this post with comment 
            new_comment.save()#save new comment in db 
    else:
        comment_form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids.exclude(id=post.id))
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]    
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 
                                                'new_comment': new_comment,
                                               'comment_form': comment_form, 'similar_posts': similar_posts})

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

