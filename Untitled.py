#!/usr/bin/env python
# coding: utf-8

# for_format_list

# In[2]:


s = '{} {} {}'
s.format


# In[4]:


s= '{}이는{}와{}흘 좋아해'
pr=s.format('쉣','쉣2','쉣3')
print(pr)


# In[5]:


s= '{}이는{}번이고{}대학에 갔어'
pr=s.format('쉿',33333,'홀리')
print(pr)


# ###[문제]햄버거 1개는 4달라###

# In[6]:


s= '{} {}개는 {}달라'
pr=s.format('햄버거',1,4)
print(pr)


# In[7]:


food = '햄버거'
num = 2
doolar = num*4
s= '{} {}개는 {}달라'
pr=s.format(food,num,doolar)
print(pr)


# In[13]:


food = list(map(int,input('햄버거 개수 가격(순서대로)>>').split()))
num = int(food[0])
doolar = num*int(food[1])
s= '{} {}개는 {}달라'
pr=s.format('햄버거',num,doolar)
print(pr)


# In[16]:


stu = '%s %d학년 %s'
pr = stu%('인천여상',3,'김고은')
pr


# In[23]:


juso = '     인천시 연수구 동춘동      '
juso


# In[18]:


type(juso)


# In[20]:


add=juso.strip()


# In[21]:


juso


# In[22]:


add


# In[24]:


len(add)


# In[25]:


len(juso)


# In[26]:


add.split()


# In[29]:


add.endswith('동춘동')


# In[30]:


add.startswith('인천')


# In[31]:


num=10
if num==10:
    print('숫자10')
else:
    print('10아님')


# In[32]:


num=int(input())
if num%2==0:
    print('퓅수')
else:
    print('웤후맨')


# In[33]:


sum = 0
for i in range(20,31):
    if i%2 !=0:
        sum+=i
        print(i)
print("홀수합 > ",sum)


# #[문제만들기]
# for if 포함

# In[40]:


num = int(input())
hsum = 0;
jsum = 0;
for i in range(1,num+1):
    if i%2==0:
        hsum+=i;
    elif i%2!=0:
        jsum+=i;
    print(i)
print("홀수 합",hsum)
print("짝수 합",jsum)
print("둘의 합",hsum+jsum)


# In[ ]:




