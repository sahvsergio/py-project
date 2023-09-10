import requests
def get_categories():
    r= requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) #the type for thi is a string we need to make it a json
    categories=r.json()#transforms response to python
    
    #loop through categories#
    for caegory in categories:
        print(category['name'])
        
        
        