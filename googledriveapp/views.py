from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Folder, File
############################
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

# Model imports
from googledriveapp.models import Folder,File
# Create your views here.
# Main page for our drive clone with folders in it where user can click and go to the specific folder 
def index(request):
    if request.user.is_authenticated:
        folder = Folder.objects.filter(folderuser=request.user)
        context = {'folder':folder}
        return render(request,'index.html',context)
    else:
        return redirect('signup')
# Folder with files in it
def folder(request,folderid):
    if request.user.is_authenticated:
        folder_user = Folder.objects.get(id=folderid)
        files = File.objects.filter(folder=folder_user)
        context = {'folderid':folderid,'files':files}
        if request.method == 'POST':
            file_user = request.FILES.get('file')
            file_title = request.POST.get('filetitle')
            fileadd = File.objects.create(filetitle=file_title,file=file_user,folder=folder_user)
        return render(request,'folder.html',context)
    else:
        return redirect('signup')
# Add Folder View
def addfolder(request):
   if request.method == 'POST':
       folder_name = request.POST['foldername']
       folder_desc = request.POST['desc']
       folder = Folder.objects.create(foldername=folder_name,folderdesc=folder_desc,folderuser=request.user)
       if folder:
           return redirect("index")
       else:
            messages.error(request,"Folder Not Created")
            return redirect("index")
# View For SignUp the user
def SignUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
            firstname = request.POST['fname']
            lname = request.POST['lname']
            if username and password and email and cpassword and firstname and lname:
                if password == cpassword:
                    user = User.objects.create_user(username,email,password)
                    user.first_name = firstname
                    user.last_name = lname
                    user.save()
                    if user:
                        messages.success(request,"User Account Created")
                        return redirect("login")
                    else:
                        messages.error(request,"User Account Not Created")
                else:
                    messages.error(request,"Password Not Matched")
                    redirect("signup")
        return render(request,'signup.html')
    
# View For Log in the user
def Login(request):
    if request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username and password:
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return redirect('index')
        return render(request,'login.html')
# User logout function
def Logout(request):
    logout(request)
    return redirect("index")

######################
def delete_file(request, file_id):
    if request.method == 'POST':
        # Get the file object
        file_to_delete = get_object_or_404(File, id=file_id)

        # Check if the user has permission to delete this file
        if file_to_delete.folder.folderuser == request.user:
            # Delete the file
            try:
                file_to_delete.file.delete()
                file_to_delete.delete()
                print("File deleted successfully.")
                return JsonResponse({'message': 'File deleted successfully.'}, status=200)
            except Exception as e:
                print("Error:", str(e))
                return JsonResponse({'error': f'Unable to delete file: {str(e)}'}, status=400)
        else:
            print("User does not have permission to delete this file.")
            return JsonResponse({'error': 'You do not have permission to delete this file.'}, status=403)
        
    print("Invalid request method.")
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
############################################
def rename_file(request, file_id):
    if request.method == 'POST':
        new_file_title = request.POST.get('new_file_title', '')

        if new_file_title:
            file_to_rename = get_object_or_404(File, id=file_id)

            if file_to_rename.folder.folderuser == request.user:
                file_to_rename.filetitle = new_file_title
                file_to_rename.save()
                return JsonResponse({'message': 'File renamed successfully.'}, status=200)
            else:
                return JsonResponse({'error': 'You do not have permission to rename this file.'}, status=403)
        else:
            return JsonResponse({'error': 'New file title cannot be empty.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)