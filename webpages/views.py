from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    User = get_user_model()
    detail = User.objects.all()
    # audio_feature_endpoint = requests.get('http://127.0.0.1:8000/api/v1')
    # print(audio_feature_endpoint.json())
    data ={
        'detail': detail,
    }    
    return render(request, 'webpages/home.html', data)

def delete_user(request, id):
    print(request.user.username)
    User = get_user_model()
    del_user = User.objects.get(pk = id)
    del_user.delete()
    messages.success(request, 'Successfully deleted')
    return redirect('home')

def edit_user(request, pk):
    User = get_user_model()
    ed_user = User.objects.get(pk=pk)
    data = {
        'ed_user': ed_user,
    }
    if request.method == 'POST':
        ed_user.email = request.POST['email']
        ed_user.username = request.POST['username']
        ed_user.address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            ed_user.password = password
    
        ed_user.save()
        messages.success(request, 'Successfully edited user details')
        return redirect('home')
    
    return render(request, 'webpages/edit_page.html', data)