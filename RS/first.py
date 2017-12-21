import csv
import math
import requests
import json
#***********
OurUser = 36  # расчитываем оценку для этого пользователя
#rчитаем файл и записываем данные в список
file="data.csv"
listt = []
dif_list=[]
f=open(file)
for i in csv.reader(f):
    listt.append(i)
    dif_list.append(i)
f.close()
print(listt)
#количество фильмов
CountOfMovies=(len(listt[0]))
print(CountOfMovies)
print(listt[0])
#simUV function
'''
проходим по всем фильмам
если у пользователя отрицательная оценка,то не берем его в расчет
иначе считаем ценку пользователя согласно формуле simUV
'''
def simUV(u,v):
    Ui,Vi,uv=0,0,0
    for i in range(1,CountOfMovies):
        if(int(listt[u][i])!=-1 and int(listt[v][i])!=-1):
           Ui+=math.pow(int(listt[u][i]),2)
           Vi += math.pow(int(listt[v][i]), 2)
           uv+=int(listt[u][i])*int(listt[v][i])
    sim=uv/(math.sqrt(Ui)*math.sqrt(Vi))
    return sim
#функция подсчета средней оценки
'''
подсчитываем среднюю оценку для некоторого пользователя:
если фильм был просмотрен(то есть оценка не -1),тогда суммируем оценки и количество фильмов
и возращаем среднее значение
'''
def middle(person):
    summ,count=0,0
    for i in range(1,CountOfMovies):
        if(int(listt[person][i])>0):
            summ+=int(listt[person][i])
            count+=1
    return  round((summ/count),2)

#рассчитываем
'''
создаем словарь среднего значения для пользователя(avg)
создаем словарь схожей оценки(также сортируем и выбираем 5)
'''
avg={}
similirList={}
for i in range(1,len(listt)):
    avg[i] = middle(i)
    if OurUser!=i:
        similirList[i]=round(simUV(OurUser,i),2)
l = lambda x: x[1]
similirList=sorted(similirList.items(), key=l,reverse=True)[:5]
print((similirList))
#print((avg))
print("***")
#cсредняя оценка для моего пользователя
MiddleMarksForOurUser=(middle(OurUser))
print(MiddleMarksForOurUser)
#основная функция рассчета фильмов
'''
проходим по всем фильмам
    для не оценненых фильмов.
    далее,проходим по пользователям с высчитанной сходимостью.
    проверка если фильм не был оценен.
    и также по формуле высчитываем оценку
'''
def recommendation(similirList):
    result={}
    for i in range(1, len(listt[0])):

        if((listt[OurUser][i])==' -1'):
            chisl = 0
            znam = 0
            for j in similirList:
                #print(listt[j[0]][i])
               # print(avg[j[0]])
                if (listt[j[0]][i]) != ' -1':
                     #print(j[1])

                     chisl+=j[1]*(int(listt[j[0]][i])-avg[j[0]])
                     znam+=j[1]
            result[i]= MiddleMarksForOurUser+round((chisl/znam),2)
    return result
a=recommendation(similirList)
print(a)
#end of first task
#************************
#second task
print("****************************************************************************************************************")
#читаем файл
cont_file="context.csv"
newList = []
f=open(cont_file)
for i in csv.reader(f):
    newList.append(i)
f.close()
#print(newList)
#количество фильмов
CountOfMovies=(len(newList[0]))
#print(CountOfMovies)
#print(newList[0])
#так как надо посоветовать в будний день,то исключим выходные дни
for i in range(1,len(listt)):
    for j in range(1,len(dif_list[0])):
        if (newList[i][j]==' Sat' or newList[i][j]==' Sun'):
                dif_list[i][j]=' -2'
print(dif_list)
#аналогично первой задаче используем метрику схожести и среднее значение
list={}
avgcont={}
for i in range(1,len(dif_list)):
    avgcont[i] = middle(i)
    if OurUser!=i:
        list[i]=round(simUV(OurUser,i),2)
l = lambda x: x[1]
#выьираем 5 лучших схожих
list=sorted(list.items(), key=l,reverse=True)[:5]
print((list))
print(avgcont)
#используем функцию подсчета оценки
#выбираем одну лучшую из них
b=recommendation(list)
b=sorted(b.items(),key=l,reverse=True)[:1]
print(b)
#end of second task
#********************
#ывод в формате json
format='https://cit-home1.herokuapp.com/api/rs_homework_1'
json={
        "user":36,
        "1":{
            "movie 3": 3.22,
            "movie 16": 3.61,
            "movie 17":2.33,
            "movie 18": 3.01,
            "movie 20": 2.96,
            "movie 21": 2.05

            },
    "2":
        {
            "movie 20":4.55
        }
    }
head={'content-type':'application/json'}
#print((requests.post(format,json=json,headers=head)).json())