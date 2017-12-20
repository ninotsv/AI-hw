import requests


#оформляем ответ
format='https://cit-home1.herokuapp.com/api/ga_homework'
'''json={
        "user":36,
        "1":{
                #"item":BackPack,
                "weight":weightRes,
                "size":round(SizeRes,2),
                "price":someth[1]
            }
    }'''
json={
        "user":36,
        "1":{
                "items":BackPack,
                "weight":weightRes,
                "volume":round(SizeRes),
                "value":someth[0]
            }
    }
head={'content-type':'application/json'}
print((requests.post(format,json=json,headers=head)).json())

