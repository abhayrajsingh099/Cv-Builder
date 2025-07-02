from django.shortcuts import render,redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        linkedin = request.POST.get("linkdin","")
        github = request.POST.get("github","")
        project_1 = request.POST.get("project_1","")
        project_2 = request.POST.get("project_2","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        experience = request.POST.get("experience","")
        skills = request.POST.get("skills","")
        frameworks = request.POST.get("frameworks","")

        # profile = Profile(name=name,email=email,phone=phone,linkedin=linkedin,github=github,project_1=project_1,project_2=project_2,degree=degree,school=school,university=university,previous_work=experience,skills=skills,frameworks=frameworks)
        Profile.objects.create(name=name,email=email,phone=phone,linkedin=linkedin,github=github,project_1=project_1,project_2=project_2,degree=degree,school=school,university=university,previous_work=experience,skills=skills,frameworks=frameworks)
        return redirect('list')

    return render(request,'cvapp/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('cvapp/resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'encoding': "UTF-8",
        'quiet': '',
        'no-outline': None,
        'dpi': 300,
        'zoom': '1.3',
        'enable-local-file-access': '',
    }
    pdf = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"

    return response

def list(request):
    profile = Profile.objects.all()

    return render(request,'cvapp/list.html',{'profiles':profile})