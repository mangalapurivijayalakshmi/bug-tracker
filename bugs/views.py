from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from bugs.models import *
from .forms import BugForm
from django.contrib.auth.decorators import login_required

# Show all bugs
@login_required
def bug_list(request):
    bugs = Bug.objects.filter(created_by=request.user)
    return render(request, 'bugs/bug_list.html', {'bugs': bugs})

# Create a new bug
@login_required
def bug_create(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.created_by = request.user
            bug.save()
            return redirect('bug_list')
    else:
        form = BugForm()
    return render(request, 'bugs/bug_form.html', {'form': form})

# Update bug status
@login_required
def bug_update(request, pk):
    bug = Bug.objects.get(id=pk)
    if request.method == 'POST':
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugForm(instance=bug)
    return render(request, 'bugs/bug_form.html', {'form': form})