from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def say_hello(request):  # url = http://127.0.0.1:8000/hello/name=Jennifer
	# return HttpResponse('Hello')
	input_name = request.GET.get('name',"")
	# talk = ""
	# for i in range(3):
	# 	talk = talk + 'hello' + input_name + '\n'
	if input_name == "":
		return HttpResponse("Please enter name")
	return render(request,"index.html",{"name":input_name})

def index(request):
	if request.method == 'GET':
		print('---This is a get request')
		return render(request,"index.html")
	else:
		print('---This is a post request')
		input_username = request.POST.get("username","")
		input_password = request.POST.get("password","")
		print('---name:',input_username) 
		print('---pwd:',input_password)
		if input_username == "" or input_password == "":
			return render(request,"index.html",{"error":"用户名或密码为空"})
		
		user = auth.authenticate(username=input_username,password=input_password)
		if user is None:
			return render(request,"index.html",{"error":"用户名或密码错误"})
		else:
			auth.login(request,user) # save user login status
			return HttpResponseRedirect("/project/")

@login_required
def logout(request): 
	auth.logout(request) # delete user login status
	return HttpResponseRedirect("/index/")