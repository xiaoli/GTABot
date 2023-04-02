from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import Subject, Paper

@login_required(login_url='/admin/login/')
def index(request):
    paper_list = Paper.objects.all().order_by('-published_date')
    return render(request, "index.html", {"paper_list": paper_list})

@login_required(login_url='/admin/login/')
def subjects(request):
    subjects = Subject.objects.all()
    return render(request, "subjects.html", {"subjects": subjects})

@login_required(login_url='/admin/login/')
@csrf_exempt
def mark_as_read(request):
    paper_id = request.GET['pid']
    p = get_object_or_404(Paper, id=paper_id)
    p.is_read = True
    p.save()
    
    data = {
        "status": "ok"
    }
    return JsonResponse(data, safe=False)