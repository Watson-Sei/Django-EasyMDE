from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User


class Index(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request):
        post = Post.objects.all()
        context = {
            'post': post
        }
        return self.render_to_response(context)

class PostDetail(TemplateView):
    template_name = 'blog/detail.html'
    def get(self, request, **kwargs):
        print(self.kwargs['pk'])
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        context = {
            'post_detail':post
        }
        return self.render_to_response(context)



class Edit(View):

    def get(self, request, **kwargs):
        form = PostForm()
        context = {
            'form': form,
        }
        return render(request, 'blog/edit.html', context)

    def post(self, request, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = get_object_or_404(User, pk=1)
            form.save()
            return redirect('/')
        return render(request, 'blog/edit.html', {'form': PostForm()})
