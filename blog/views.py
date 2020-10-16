import time
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Tag
import base64
# Create your views here.
def index(request):
    posts = Article.objects.all()[:5]
    allposts = Article.objects.all()
    return render(request, 'index.html', {'posts':posts,'allposts':allposts})

def list(request):
    posts = Article.objects.all()
    ranks = Article.objects.all()[:8]
    tags = Tag.objects.all()[:9]
    return render(request, 'list.html', {'posts':posts, 'ranks':ranks, 'tags':tags})

def info(request,pk):
    post = get_object_or_404(Article, pk=pk)
    ranks = Article.objects.all()[:8]
    tags = Tag.objects.all()[:9]
    allposts = Article.objects.all()
    return render(request, 'info.html', {'ranks':ranks, 'post':post, 'tags':tags, 'allposts':allposts})

def taglist(request,pk):
    posts = Article.objects.filter(tags_id=pk)
    posttag = Article.objects.filter(tags_id=pk)[0]
    ranks = Article.objects.all()[:8]
    tags = Tag.objects.all()[:9]
    return render(request, 'taglist.html',{'ranks':ranks, 'posts':posts, 'tags':tags, 'posttag':posttag})

def about(request):
    return render(request, 'about.html')

def search(request):
    if request.method == 'POST':
        keyboard = request.POST.get('keyboard', '')
        posts = Article.objects.filter(title__icontains=keyboard)
        ranks = Article.objects.all()[:8]
        tags = Tag.objects.all()[:9]
        return render(request, 'search.html', {'posts':posts, 'ranks':ranks, 'tags':tags})

def test(request):
    if request.method == 'POST':
        img = request.POST.get('img')
        ines = img.split('base64,')
        imgdata = base64.b64decode(ines[1])
        timestamp = str(int(time.time()))
        file_url = 'static/upload/%s.%s' % (timestamp, 'jpg')
        leniyimg = open(file_url, 'wb')
        leniyimg.write(imgdata)
        leniyimg.close()
        print(img)
        return HttpResponse('返回成功')
    return render(request, 'upload.html')