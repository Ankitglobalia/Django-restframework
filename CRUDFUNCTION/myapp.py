
import requests
import json

URL = "http://127.0.0.1:8000/studentApi/"

def get_data(id = None):

    data = {}
    if id is not None:
        data = {'id':id}
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)

    r=requests.get(url=URL,headers=headers,data=json_data)
    
    data=r.json()
    print(data)       

get_data()

def post_data():

    data = {'id': 4,'name': 'sai','roll':104,'city':'pune'}
    headers={'content-type':'application/json'}

    json_data=json.dumps(data)

    r = requests.post(url= URL,headers=headers ,data=json_data)

    data=r.json()

    print(data)

# post_data()    



def update_data():
    data = {'id':4,'name':'Ram','roll':105,'city':'surat'}
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r = requests.put(url= URL,headers=headers, data = json_data)

    data = r.json()
    print(data)

# update_data()    


def Delete_data():

    data = { 'id':4,
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    r = requests.delete(url= URL,headers=headers ,data=json_data)
    data = r.json()
    print(data)
# Delete_data() 

