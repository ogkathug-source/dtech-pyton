 my_dict={"name";"nelson";"age";30,"tribe":"somali"}






backup=my_dict.copy()
print(backup)

keys=["name","age","city"]
value="unknown"
default=dict.fromkeys(key,values)
print(default)




getting=backup.ge("age")
print(getting)

value=my_dict.values()
print(value)




poping=backup.pop("name")
print(poping)
print(backup)

popitem=my_dict.popitem()
print|(popitem)
print(my_dict)


new_dict={"name":"lenox","country":"kenya"}
setdefaulting=new_dict.setdefault("name","Giriama")
print(setdefaulting)

updating=my_dict.update(new_dict)
print(my_dict)


new_key=["school","gender","class"]
new_values=[]
