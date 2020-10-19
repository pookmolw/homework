from django.db import models
from django.utils import timezone
from module_app.models import Module

class Testcase(models.Model):
	'''
	测试用例表
	'''
	module = models.ForeignKey(Module,on_delete=models.CASCADE) #删除关联数据与之关联的也删除
	name = models.CharField("名称",max_length=50,null=False)
	url = models.TextField("请求地址",null=False)
	method = models.IntegerField("请求方式",default=1,null=False) #get=1 post=2 put=3 delete=4
	header = models.TextField("请求头",default="")
	parameter_type = models.IntegerField("参数类型",default=1,null=False) #form=1 json=2
	parameter_body = models.TextField("参数",default="",null=False)
	result = models.TextField("返回结果",default="",null=False)
	assert_type = models.IntegerField("断言类型",default=1,null=False) #contains=1 match=2
	assert_text = models.TextField("断言",default="",null=False)
	assert_result = models.TextField("断言结果",default="",null=False)
	create_time = models.DateTimeField("创建时间",auto_now_add=True)
	update_time = models.DateTimeField("更新时间",auto_now=True)

	def __str__(self):
		return self.name
