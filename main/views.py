from django.http import JsonResponse
from main.models import Post
# Create your views here.


def homepage(request):
    posts = Post.objects.all().values('Header', 'Content', 'SubTitile', 'ImgURL')
    resPosts=list(posts)
    return JsonResponse(resPosts, safe=False)
