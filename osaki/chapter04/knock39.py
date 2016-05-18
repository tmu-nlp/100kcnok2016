#-*- coding:utf-8 -*-
import re
import numpy
import matplotlib.pyplot as plt
from collections import defaultdict
d=defaultdict(lambda:0)
dw=defaultdict(lambda:0)
l=list()
c=0
x=[]
y=[]

for line in open("neko.txt.mecab","r"):
    if line == "EOS\n":
        continue
    line=re.sub(",,*",",",line.replace("\t"," ").replace(" ",","))
    d={}
    d["表層形"]=line.split(",")[0]
    d["基本形"]=line.split(",")[-3]
    d["品詞"]=line.split(",")[1]
    d["品詞細分類１"]=line.split(",")[2]
    l.append(d)

for words in l:
    dw[words["基本形"]]=dw[words["基本形"]]+1

for foo,bar in sorted(dw.items(),key=lambda x:x[1],reverse=True):
    c+=1
    y+=[bar]
    x+=[c]

plt.xscale("log")
plt.yscale("log")
plt.scatter(x,y)
plt.show()
