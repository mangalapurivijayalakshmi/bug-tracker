from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from bugs.models import Bug
from .forms import BugForm, BugEditForm


# Show all bugs (created by the logged-in user)
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


# Update bug (status, priority, assignment)
@login_required
def bug_update(request, pk):
    # Only allow the user who created the bug to edit it
    bug = get_object_or_404(Bug, id=pk, created_by=request.user)

    if request.method == 'POST':
        form = BugEditForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('bug_list')
    else:
        form = BugEditForm(instance=bug)
    return render(request, 'bugs/bug_form.html', {'form': form})


# Delete a bug
@login_required
def bug_delete(request, pk):
    bug = get_object_or_404(Bug, id=pk, created_by=request.user)
    if request.method == 'POST':
        bug.delete()
        return redirect('bug_list')
    return render(request, 'bugs/bug_confirm_delete.html', {'bug': bug})
