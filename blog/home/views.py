from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category
from .forms import NewPostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def LikesView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post',args=[str(pk)]))


class Home(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-created_on']
    #ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_like()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPost(CreateView):
    model = Post
    form_class = NewPostForm
    template_name = "addpost.html"

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "updatepost.html"
    #fields = ['title', 'body']
class DeletePost(DeleteView):
    model = Post
    template_name = "deletepost.html"
    success_url = reverse_lazy('home')

def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats).order_by('-created_on')
    cat_menu = Category.objects.all()
    return render(request, 'categories.html', {'cats':cats, 'category_post':category_post, 'cat_menu':cat_menu})