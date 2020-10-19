from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project_app.models import Project

# 项目列表页
@login_required
def project_list(request): 
	project_all = Project.objects.all()
	return render(request,"project.html",{"projects":project_all,"type":"list"})

# 创建项目
@login_required
def add_project(request):
	if request.method == "GET":
		return render(request,"project.html",{"type":"add"})
	elif request.method == "POST":
		name = request.POST.get("name","")
		describe = request.POST.get("describe","")
		status = request.POST.get("status","")
		if name == "":
			return render(request,"project.html",{"type":"add","name_error":"项目名称不能为空"})
		p = Project.objects.create(name=name,describe=describe,status=status)
		p.save()
		return HttpResponseRedirect("/project/")

# 编辑项目
@login_required
def edit_project(request,pid):
	# print("--edit_project--method:" + request.method)
	if request.method == "GET":
		p = Project.objects.get(id=pid)
		form = ProjectForm(instance=p)
		return render(request,"project.html",{"type":"edit","form":form,"pid":pid})
	
	elif request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			status = form.cleaned_data['status']
			p = Project.objects.get(id=pid)
			p.name = name
			p.describe = describe
			p.status = status
			p.save()
			return HttpResponseRedirect("/project/")
		else:
			return HttpResponse("Wrong")

# 删除项目
@login_required
def delete_project(request,pid):
	if request.method == "GET":
		p = Project.objects.filter(id=pid)
		p.delete()
		return HttpResponseRedirect("/project/")
	else:
		return HttpResponseRedirect("/project/")

@login_required
def get_project_list(request):
	if request.method == "GET":
		projects = Project.objects.all()
		project_list = []
		for p in projects:
			d = {"id":p.id,"name":p.name}
			project_list.append(d)
		return JsonResponse({"success":True,"status":10200,"data":project_list})
	else:
		return JsonResponse({"data":"请求方式错误","status":10400,"success":False})