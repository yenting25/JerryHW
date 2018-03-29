
# coding: utf-8

# In[4]:


from sources import calculator as c
#from sources import calculator import func_add
#from calculator import func_minus
#from calculator import func_cross
#from calculator import func_div
y=input()
a=list(y)
if '+' in a:
    x=y.split('+')
if '-' in a:
    x=y.split('-')
if '*' in a:
    x=y.split('*')
if '/' in a:
    x=y.split('/')

if '+' in a:
    print(c.calculator(x[0] ,x[1] , c.func_add))
if '-' in a:
    print(c.calculator(x[0],x[1],c.func_minus))
if '*' in a:
    print(c.calculator(x[0],x[1],c.func_cross))
if '/' in a:
    print(c.calculator(x[0],x[1],c.func_div))
    

