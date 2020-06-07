Ajax不会刷新页面，因此可以只更新部分内容。

实现前后端分离，后端返回数据，

$.get(url，参数，function(){});

Ajax，jQuery ，js的关系？

实现一个计算器的页面。

在<head>引用jQuery

Django新建一个app，设计前端页面，添加url，添加settings app，写后端方法

定位元素：(获取元素值,赋值)

document.queeySelector(定位).value

监听元素：

$(标签).操作(function(){});

触发：

标签加属性onclick，属性值调用js方法。

js方法定义在<script>内。

后端方法：接受request请求，获得前端传来的参数，进行处理，使用JsonResponse返回数据。后端验证参数是否正确，错误设计错误提示和错误码。

前端js：

获取前端的参数，ajax请求后端处理，获取后端得结果，展示在页面。前端判断输入参数是否合法，不合法则在前端显示提示。