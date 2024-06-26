from django.shortcuts import render,get_object_or_404
from.models import chaiVarity,Store
from .forms import chaiVarityForm
from.models import About,Skill,Resume,Socalmedia
# Create your views here.

def all_chai(request):
    chais=chaiVarity.objects.all()
    return render(request,'chai/all_chai.html',{'chais':chais})

def chai_details(request,chai_id):
    chai=get_object_or_404(chaiVarity,pk=chai_id)
    return render(request,'chai/chai_datails.html',{'chai':chai})

def chai_store_view(request):
    stores=None
    if request.method=='POST':
        form=chaiVarityForm(request.POST)
        if form.is_valid():
           chai_varity= form.cleaned_data['chai_varity']
           stores=Store.objects.filter(chai_varietes=chai_varity)
    else:
        form=chaiVarityForm()       

    return render(request,'chai/chai_stores.html',{'stores':stores,'form':form})

#Index page view
def home(request):
    about=About.objects.all()
    skill=Skill.objects.all()
    resume=Resume.objects.all()
    socal_media=Socalmedia.objects.all()
    
    return render(request,'index.html',{'abouts':about,'skills':skill,'resumes':resume,'socal_media':socal_media})
