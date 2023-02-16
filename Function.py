def hello():
    print( "this is my first function")

hello()
def calculate():
    x=3
    y=8
    print(x*y)

calculate()

def names(fname,lname):
    print(fname+" "+lname)

names("Anto","Maina")
names("Walter","Jesse")
names("Edith","Korir")

def greetings(name, greeting="Hello"):
    print(greeting+" "+name)

greetings("Erick")

def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,2,4,8,17,98)
print(result)

def minvalue(e,d,f,c,g):
    return min(e,d,f,c,g)
point=minvalue(4,5,7,2,98)
print(point)

def got(character,favourite=" John Snow"):
    print(favourite+" "+character)
got("was the last dragon")

def sort_list(lst):
    return sorted(lst)
answer=sort_list([1,3,6,8,4,53])
print(answer)

def print_num(n):
    for i in range(n):
        print(i)

print_num(5)

