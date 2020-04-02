from datetime import datetime
import requests

def get_time(timestamp):
    timestamp/=1000
    dt_object = datetime.fromtimestamp(timestamp)
    return str(dt_object)

def get_history(link):
    ses=requests.session()
    headers={"cookie": "__cfduid=dc84d0f205df35cc01f4955837d57634f1582898880; _ga=GA1.2.1997875212.1582898905; _gid=GA1.2.1447958284.1582898905; _gat_gtag_UA_50001635_52=1; XSRF-TOKEN=eyJpdiI6IjRqc1lcL2F3Tnp4UnZubW9KY0dqWjJBPT0iLCJ2YWx1ZSI6InJYTG5kaEFURmRPUWhSclp2RlZIK25icmVMTWVScHdxMlk3T1BBQmdjM0hkZWRLbElUNDRaamw4M1ROT3M3dEgiLCJtYWMiOiJjOWQ3NzMxZWRkZGYzODEwMTVjOWUzNTg3MTU5YTliMGZiYzllYmYzYjIzODUxYzEyNjFmMjY0MmNjMmVjMTNkIn0%3D; pricehistory_session=eyJpdiI6IndpanAzY1ZhbE9VKzYwSUNjb0pEd3c9PSIsInZhbHVlIjoiQXM5eWJZeTI1cUhMTnl4VU14QVR2QThBZ05yZkM5Q05nb2NFZXBVeVlUQXVMRmRXaDFNYzBTdGZRelRISkZQRyIsIm1hYyI6IjIzY2Y0NDA4ZDQ3OTRkMWNiM2U2MGJkNDFkMWQ4ZWY1NTNiYzc5YTU4ZDdhMzMyMWE3Njc0MjA4ZjBiNmIyMWQifQ%3D%3D",
             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
    ses.headers.update(headers)
    res1=ses.get('https://pricehistory.in/')
    data={"product_url": link,
            "_token": "eoVrhBzfJvidvwPUf5yrsvV0qT62UPRYFDqeGA40"}
    res=ses.post('https://pricehistory.in/api/productHistory',data=data).json()
    data={}
    try:
        data['product']=res['title']
        data['store']=res['store']
        data['avg_price']=res['avg_price']
        data['low_price']=res['low_price']
        data['high_price']=res['high_price']
        data['curr_price']=res['curr_price']
        data['time']={}
        data1=res['data'][2:-2].split('],[')
        for i in data1:
            i=i.split(',')
            time=get_time(int(i[0]))
            try:
                data['time'][time]=int(i[1])
            except Exception:
                data['time'][time]=float(i[1])
    except Exception as e:
        print(str(e))
    return data

def get_date(list,search):
    search=int(search)
    arr=[]
    for time in list.keys():
        cost=int(list[time])
        if cost == search:
            arr.append(time)
    return arr
'''
link=input("enter the link:   ")
data=get_history(link)
print('\n','-'*30)
min_date=get_date(data['time'],data['low_price'].replace(',',''))
max_date=get_date(data['time'],data['high_price'].replace(',',''))

print("product:",data['product'],'::',data['store'])
print("avg_price for this product is",data['avg_price'])
print("max_price for this product is",data['high_price'])
print("current price for this product is",data['curr_price'])
print("min_price for this product is",data['low_price'],'on',min_date[-1])
print('\n','-'*50)'''


ses=requests.session()
res=ses.get('https://pricehistory.in/')
token='VuU9XBbPu8ISDsAjCstlDAKNN5cERGe2pPRG9N8O'
res = ses.post('https://pricehistory.in/api/productHistory',data={'product_url':"https://www.amazon.in/Redmi-8A-Dual-Blue-Storage/dp/B07X4R63DF/ref=pd_rhf_se_p_img_1?_encoding=UTF8&psc=1&refRID=DWG7G1XGSHDD5EA5HA9H","_token":token})
print(res.text)
