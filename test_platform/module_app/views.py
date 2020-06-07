from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from module_app.models import Module
from module_app.forms import ModuleForm

# 模块列表
@login_required
def module_list(request):
	module_all = Module.objects.all()
	return render(request,"module.html",{"modules":module_all,"type":"list"})

# 创建模块
@login_required
def add_module(request):
	if request.method == "GET":
		form = ModuleForm()
		return render(request,"module.html",{"type":"add","form":form})

	elif request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			Module.objects.create(project=project,name=name,describe=describe)
		return HttpResponseRedirect("/module/")

# 编辑模块
@login_required
def edit_module(request,mid):
	if request.method == "GET":
		m = Module.objects.get(id=mid)
		form = ModuleForm(instance=m)
		return render(request,"module.html",{"type":"edit","form":form,"mid":mid})
	
	elif request.method == "POST":
		form = ModuleForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			describe = form.cleaned_data['describe']
			project = form.cleaned_data['project']
			m = Module.objects.get(id=mid)
			m.name = name
			m.describe = describe
			m.project = project
			m.save()
			return HttpResponseRedirect("/module/")
		else:
			return HttpResponse("Wrong")


# 删除模块
@login_required
def delete_module(request,mid):
	if request.method == "GET":
		m = Module.objects.filter(id=mid)
		m.delete()
		return HttpResponseRedirect("/module/")
	else:
		return HttpResponseRedirect("/module/")

@login_required
def get_module_list(request):
	if request.method == "POST":
		pid = request.POST.get("pid","")
		if pid == "":
			return JsonResponse({"data":"项目id为空","status":10401,"success":False})
		
		modules = Module.objects.filter(project=pid)
		module_list = []
		for m in modules:
			d = {"name":m.name,"mid":m.id}
			module_list.append(d)
		# print(module_list)
		return JsonResponse({"data":module_list,"status":10200,"success":True})
	else:
		return JsonResponse({"data":"请求方式错误","status":10400,"success":False})

	