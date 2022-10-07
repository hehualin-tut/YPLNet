# -*-coding:utf-8-*-
import matplotlib.pyplot as plt
x_label=['D00','D10','D20','D40']
#x_kedu
x1_data=[1,2,3,4]
x2_data=[i+0.3 for i in x1_data]
x3_data=[i+0.15 for i in x1_data]
#y_zuobiao
y1_data=[3389,3468,5802,3578]#zengqiang
y2_data=[3241,3244,4884,1789]#yuanshi

# for i in range(len(x_label)):
plt.xticks(x3_data,x_label)
p1=plt.bar(x1_data, y2_data,lw=0.5,width=0.3,fc=(1,0.5,0.25),label = 'Ori')
plt.bar_label(p1)
p2=plt.bar(x2_data, y1_data,lw=0.5,width=0.3,fc=(0,0.8,0.6),label = 'Aug')
plt.bar_label(p2)

plt.title('')#Road damage classes distribution befor and after data augmention
plt.xlabel("Types of Road Damages")
plt.ylabel("Instances")
plt.legend()
plt.show()

