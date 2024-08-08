import requests

req = requests.get('https://www.imdb.com/news/top?ref_=nv_tp_nw')

print("Headers:", req.headers)
print("Content:", req.text[:500])  
