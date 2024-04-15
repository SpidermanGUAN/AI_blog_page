from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import redirect, get_object_or_404
from blog.models import Post
from .models import Profile

from .forms import UserRegisterForm, ProfileUpdateForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            Profile.objects.create(user=form.instance)
            # username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account has been created. You can now login"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('profile')

@login_required
def profile(request):
    user_posts = request.user.profile.get_user_posts()
    context = {
        "user_posts": user_posts,
    }
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("profile")
    return render(request, "users/profile.html", context)



