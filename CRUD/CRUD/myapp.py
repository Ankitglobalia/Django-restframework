import requests
import json

URL = "http://127.0.0.1:8000/studentApi/"

def get_data(id = None):

    data = {}
    if id is not None:
        data = {'id':id}

    json_data=json.dumps(data)

    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)       

get_data()

def post_data():

    data = {'id': 31,'name': 'sai','roll':106,'city':'pune'}
    json_data=json.dumps(data)

    r = requests.post(url= URL,data=json_data)

    data=r.json()

    print(data)

# post_data()    



def update_data():
    data = {'id':31,'name':'Ram','roll':107,'city':'surat'}
    json_data=json.dumps(data)
    r = requests.put(url= URL, data = json_data)

    data = r.json()
    print(data)

# update_data()    


def Delete_data():

    data = { 'id':37,
    }
    json_data=json.dumps(data)
    r = requests.delete(url= URL, data=json_data)
    data = r.json()
    print(data)
Delete_data() 

