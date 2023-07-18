from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    context = {"key" : "dashboard"}
    return render(request, "dashboard/index.html", context)