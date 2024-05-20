import random
import pyinputplus as pyip

with open('names.txt',encoding='utf-8') as file:
    content:str = file.read()

n = pyip.inputInt("請輸入取得名字的數量",min=0,max=200)
names:list = content.split(sep="\n")
random_names = random.choices(population=names,k=n)
for name in random_names:
    print(name,end=" ")
print()