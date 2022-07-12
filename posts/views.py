"""Posts Views"""
from time import strftime
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm 
# Utilities
from datetime import datetime

posts = [
  {
    'name':'Mont Blac',
    'user':'Cristian Paguay',
    'timestamp': datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'picture':'https://picsum.photos/200/200/?image=1036',
  },
  {
    'name':'Via Láctea',
    'user':'C.Vander',
    'timestamp': datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'picture':'https://picsum.photos/200/200/?image=903',
  },
  {
    'name':'Nuevo auditorio',
    'user':'Thenpiannartist',
    'timestamp': datetime.now().strftime('%b %dth, %Y -%H:%M hrs'),
    'picture':'https://picsum.photos/200/200/?image=1076',
  },
]
@login_required
def list_posts(request):
    content=[]
    print(posts)
    for post in posts:
        content.append(f"""
                <p><b>{post['name']}</b><p>
                <p><small>{post['user']} - <i> {post['timestamp']}</i></small></p>
                <figure><img src='{post['picture']}'/></figure>  
        """)
        #.format(**post))
    return render(request,'posts/feed.html',{'posts':posts})
   # return HttpResponse('<br/>'.join(content))


@login_required
def create_posts(request):
  """Create new post view"""
  if request.method == 'POST':
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('feed')
  else:
    form=PostForm()

  return render(
      request= request,
      template_name = 'posts/new.html',
      context = {
          'form':form,
          'user':request.user,
          'profile':request.user.profile
          
          }
  )