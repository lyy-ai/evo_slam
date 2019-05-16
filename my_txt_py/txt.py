#!/usr/bin/python
# coding=utf-8

import string
import numpy
#import pandas

f1=open("data.txt",'r')#打开要替换的文件 
f1=f1.read()
f2=f1.replace(","," ") 
f3=open("new.txt","wb")#替换成功后的文件 
f3.write(f2) 
f3.close()
