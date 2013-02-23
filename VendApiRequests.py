import requests
import json
import pprint

barcode = 9320123006002
#barcode = input("Scan product barcode: ")

#Convert barcode to string
sku = str(barcode)

#Store URL concat with SKU to get URL for product
url = 'https://*.vendhq.com/api/products?sku='+sku

#Use Requests library to get JSON object for product
r = requests.get(url,auth=('*', '*'))

#Decodes the JSON object to nested dictionaries. 
product_data = r.json()

#Pretty print the data
#pprint.pprint(product_data)

#Get the outlet we are interested in 
storeCheck = 1
#storeCheck = input("1 for LEU, 2 for QBN")

#Convert to correct number and define output dictionaries
storeCheck -=1
out = {}
outData = {}

#Copy relevant inventory information from Vend object to output dictionaries
for items in product_data['products']:
    outData['id'] = items['id']


    #outData['brand_name'] = ""
    
    #Get inventory for selected store
    
    #stores = items['inventory']
    #outData['inventory'] = stores[storeCheck]
    outData['inventory'] = items['inventory']

#Move in to inventory layer of dicts
stores = outData['inventory']

#Find and print the current stock level
current_count = float(stores[storeCheck]['count'])
#print current_count

#Adjust stock level based on input
stores[storeCheck]['count'] = current_count
"""input("Enter additional stock count: ")+ """ 
    
#Pretty prints the output file to be sent
pprint.pprint(outData)

#Posts the output file as a JSON object
p = requests.post(url, data=json.dumps(outData),auth=('*', '*'))
#Prints the return value
print p 
#prints the returned obect
pprint.pprint(p.json())

#Find and print the updated stock value
new_product_data = p.json()
print "New stock count:"
pprint.pprint(int(float((new_product_data ['product']['inventory'][storeCheck]['count']))))


