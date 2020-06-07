from django.db import models
from project_app.models import Project

# 创建一个表
class Module(models.Model):
	'''
	模块表
	'''
	project = models.ForeignKey(Project,on_delete=models.CASCADE) #删除关联数据与之关联的也删除
	name = models.CharField("名称",max_length=50,null=True)
	describe = models.TextField("描述",default="")
	create_time = models.DateTimeField("创建时间",auto_now_add=True)
	update_time = models.DateTimeField("更新时间",auto_now=True)

	def __str__(self):
		return self.name