import requests
import json

# GET
payload = {"key1":"value1","key2":"value2"}
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get("http://httpbin.org/get",headers=headers,params=payload)
# print(r.content)
# print(r.encoding)
# print(r.json())
# print(r.text)
# print(r.status_code)

# POST
# 发送一些编码为表单形式的数据,即form-data
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)


# 发送json
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
# print(type(payload))
# print(type(json.dumps(payload)))
r = requests.post(url, data=json.dumps(payload))
r = requests.post(url, json=payload)
print(r.text)