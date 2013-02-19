import requests
 
r = requests.get('https://*.vendhq.com/api/products', auth=('*', '*'))
data = r.json()
print data.keys()
r2= data[u'products']
print r2

#returns a dict with two kets (pagination, products), need to remove pagination and raturn the dictionary under products.
#data2 = dict(zip(r2[0::2], r2[1::2]))


                #from itertools import izip
                #i = iter(r2)
                #data2 = dict(izip(i, i))


#data2= r2.json()
