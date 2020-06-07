from django.db import models
from django.utils import timezone

# 创建一个表
class Project(models.Model):
	'''
	项目表
	'''
	name = models.CharField("名称",max_length=50,null=True)
	describe = models.TextField("描述",default="")
	status = models.BooleanField("状态",default=1)
	create_time = models.DateTimeField("创建时间",auto_now_add=True)
	update_time = models.DateTimeField("更新时间",auto_now=True)

	def __str__(self):
		return self.name
