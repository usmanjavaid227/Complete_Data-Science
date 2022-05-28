#numeric
a=10
print(a,type(a))
a=1.2
print(a,type(a))
a=1+2j
print(a,type(a))

# squence
s="hello"
print(s,type(s))
s="""
This is py_20
"""
print(s)
#### List
l=[10,'us',4.3]
l[1]="usman javaid"  ### Muteable data tupe
print(l,type(l))

#### Tuple (Immuteable)  =>  fast
t=(1,2,'g',2.4,0)
print(t,type(t))

# Dictionary data type ==> unordered data type   ++> key:value   , muteable

d={
    'name':'USman',
    'Roll':'227'
}
print(d['name'])
print(d,type(d))

# Set  unique elements
my_set={1,2,3,3}
print(my_set,type(my_set))


