from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import UserCreationForm
from blog.forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
from .forms import Myimage
from .models import Image
# Create your views here.
#hi pankaj
# Home
def home(request):
	posts=Post.objects.all()
	return render(request,'blog/home.html',{'posts':posts})
# About
def about(request):
	return render(request,'blog/about.html')
#  contact
def contact(request):
	return render(request,'blog/contact.html')
#dashbord
def dashbord(request):
	if request.user.is_authenticated:
		posts=Post.objects.all()
		user=request.user
		full_name=user.get_full_name()
		grp=user.groups.all()
		print(grp,'00000000000000000000000000')
		return render(request,'blog/dashbord.html',{'group':grp,'posts':posts,'fullname':full_name,})
	else:
		return HttpResponseRedirect('/login/')
#log_out
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('home')

#signup	
def user_signup(request):
	if request.method =='POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			group = Group.objects.get(name='Author')
			user.groups.add(group)
			messages.success(request,'!  This User Add success-fully  !')
			print('form is saved successfully  ----------------------------------------')
	else:
		form=SignupForm()
		print(' get part run signup  ----------------------------------------')
	return render(request,'blog/signup.html',{'form':form})
#login
def user_login(request):
	if not request.user.is_authenticated:
		print('login if first part run 1---------------1')
		if request.method=='POST':
			print('login if first part run 1---------------2')
			form = LoginForm(request=request,data=request.POST)
			if form.is_valid():
				print('login if first part run 1---------------3')
				uname = form.cleaned_data['username']
				upass = form.cleaned_data['password']
				user = authenticate(username=uname,password=upass)
				if user is not None:
					print('login if first part run 1---------------4')
					# messages.success(request,'! You are successfully Loged in !')
					login(request,user)
					return HttpResponseRedirect('/dashbord/')
		else:
			print('login else part run------------------------')
			form=LoginForm()
		return render(request,'blog/login.html',{'form':form})
	else:
		return HttpResponseRedirect('/dashbord/')


#add post

def add_post(request):
	if request.user.is_authenticated:
		if request.method=='POST':
			form=PostForm(request.POST)
			if form.is_valid():
				title=form.cleaned_data['title']
				description=form.cleaned_data['description']
				pst=Post(title=title,description=description)
				pst.save()
				form=PostForm()
		else:
			form = PostForm()
		return render(request,'blog/addpost.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')  

# update post

def update_post(request,id):
	if request.user.is_authenticated:
		if request.method=='POST':
			pi=Post.objects.get(id=id)
			form=PostForm(request.POST,instance=pi)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/dashbord/')

		else:
			pi=Post.objects.get(id=id)
			form=PostForm(instance=pi)
		return render(request,'blog/update.html',{'form':form})
	else:
		return HttpResponseRedirect('/login/')      

# delete post

def delete_post(request,id):
	if request.user.is_authenticated:
		posts=Post.objects.get(id=id)
		posts.delete()
		return HttpResponseRedirect('/dashbord/')
	else:
		return HttpResponseRedirect('/login/') 

def image(request):
	if request.method=='POST':
		form=Myimage(request.POST,request.FILES)
	
		if form.is_valid():
			form.save()
	
	form=Myimage()
	img=Image.objects.all()
	return render(request,'blog/image.html',{'form':form,'img':img})

def delete_image(request,id):
	image=Image.objects.get(id=id)
	image.delete()
	return redirect('image')