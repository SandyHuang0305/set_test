#增加元素方法1
thisset = set (("google", "runboo", "taobao"))
thisset.add("facebook")
print(thisset)

#增加元素方法2
thisset = set(("google", "runoob", "taobao"))
thisset.update({1,3})
print(thisset)

thisset.update({1,4},{5,6})
print(thisset)

#移除元素
thisset = set(("google", "runoob", "taobao"))
thisset.remove("taobao")
print(thisset)

#移除不存在的元素