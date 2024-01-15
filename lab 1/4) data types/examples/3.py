x = "Hello World" #str
print(x, type(x))	

x = 20	#int
print(x, type(x))	

x = 20.5	#float
print(x, type(x))

x = 1j	#complex	
print(x, type(x))

x = ["apple", "banana", "cherry"]	#list	
print(x, type(x))

x = ("apple", "banana", "cherry")	#tuple
print(x, type(x))	

x = range(6)	#range	
print(x, type(x))

x = {"name" : "John", "age" : 36}	#dict	
print(x, type(x))

x = {"apple", "banana", "cherry"}	#set	
print(x, type(x))

x = frozenset({"apple", "banana", "cherry"})	#frozenset
print(x, type(x))	

x = True	#bool	
print(x, type(x))

x = b"Hello"	#bytes	
print(x, type(x))

x = bytearray(5)	#bytearray
print(x, type(x))	

x = memoryview(bytes(5))	#memoryview	
print(x, type(x))

x = None	#NoneType
print(x, type(x))