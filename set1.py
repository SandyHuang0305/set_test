#增加元素方法1
# s.add(x)
thisset = set (("google", "runboo", "taobao"))
thisset.add("facebook")
print(thisset)

#增加元素方法2
# s.update(x)
thisset = set(("google", "runoob", "taobao"))
thisset.update({1,3})
print(thisset)

thisset.update({1,4},{5,6})
print(thisset)

#移除元素
# s.remove(x)
thisset = set(("google", "runoob", "taobao"))
thisset.remove("taobao")
print(thisset)

#移除不存在的元素不會出錯
# s.discard(x)
thisset = set(("google", "runoob", "taobao"))
thisset.discard("facebook")#不會因不存在而發生錯誤
print(thisset)

#隨機刪除一個元素
thisset = set(("google", "runoob", "taobao", "facebook"))
x = thisset.pop()
print(x)

#pop在交互模式下,會刪除最後一個元素
# s.pop()
thisset = set(("google", "runoob", "taobao", "facebook"))
thisset.pop()
print(thisset)

#計算元素個數
# len(s)
thisset = set(("google", "runoob", "taobao"))
print(len(thisset))

#清空集合
# s.clear()
thisset = set(("google", "runoob", "taobao"))
thisset.clear()
print(thisset)

#判斷元素是否存在
# x in s
thisset = set(("google", "runoob", "taobao"))
"runoob" in thisset
if "runoob" in thisset:
	print('true')
else:
	print('false')

"facebook" in thisset
if "facebook" in thisset:
	print('true')
else:
	print('false')