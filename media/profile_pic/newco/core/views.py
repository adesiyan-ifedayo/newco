from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Journal, Profile
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import JournalModelForm, JournalForm
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm, UserCreationForm

# Create your views here.
def home(request):
    template_name = 'core/home.html'
    context = {}
    return render(request, template_name, context)

# EVERYTHING JOURNAL
@login_required
def journal_list_view(request):
    template_name = 'core/journal.html'
    jn = Journal.objects.order_by("-timestamp")
    context = {'journal': jn}
    return render(request, template_name, context)


@login_required
def journal_detail_view(request, slug):
	template_name = 'core/journal_detail.html'
	jn = get_object_or_404(Journal, slug=slug)
	context ={ 'journal' : jn }
	return render(request, template_name, context)


@login_required
def journal_create_view(request):
    form = JournalModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/journal/')
        form = JournalModelForm()
    template_name = 'core/form.html'
    context = {'form': form}
    return render(request, template_name, context)  

@login_required
def journal_update_view(request, slug):
    jn = get_object_or_404(Journal, slug=slug)
    form = JournalModelForm(request.POST or None, instance=jn)
    if form.is_valid():
        form.save()
        return redirect('/journal/')
    template_name = "core/journal_update.html"
    context = {"title": f"Update {jn.content}", "form": form}
    return render(request, template_name, context)




@login_required
def journal_delete_view(request, slug):
    template_name = 'core/journal_delete.html'
    jn = get_object_or_404(Journal, slug=slug)
    if request.method == 'POST':
        jn.delete()
        return redirect('/journal')
    context ={ 'journal' : jn }
    return render(request, template_name, context)




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form':form})  




def profile(request):
    profile_form = Profile(request.POST)
    profile = Profile.objects.all()
    jn = Journal.objects.order_by('-timestamp')
    
    context={'profile_form' : profile_form, 'profile':profile, 'jn':jn}
	
    return render(request,'core/profile.html', context)

def profile_create_view(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('/profile/')
        form = ProfileUpdateForm()
    template_name = 'core/form.html'
    context = {'form': form}
    return render(request, template_name, context)     

def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if  u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()  
            messages.success(request, f'Your account has been Updated!')
            return redirect('/profile')                        
    else:    
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'core/profile_update.html', context)

