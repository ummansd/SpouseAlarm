import requests
import json

from fake_useragent import UserAgent

def get_broadcasters():
    _header = {
        'Client-Id':'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }

    _json = {
        "operationNam":"CommunityTab",
        "extensions":{
            "persistedQuery":{
                "version":1,
                "sha256Hash":"2e71a3399875770c1e5d81a9774d9803129c44cf8f6bad64973aa0d239a88caf"
            }
        },
        "variables":{
            "login":"steelohs"
        }
    }
    
    r = requests.post('https://gql.twitch.tv/gql', headers=_header, json=_json)

    return json.loads(r.text)['data']['user']['channel']['chatters']['broadcasters']

def get_title():
    _header = {
        'Client-Id':'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }

    _json = {
        "operationNam":"StreamMetadata",
        "extensions":{
            "persistedQuery":{
                "version":1,
                "sha256Hash":"a647c2a13599e5991e175155f798ca7f1ecddde73f7f341f39009c14dbf59962"
            }
        },
        "variables":{
            "channelLogin":"steelohs"
        }
    }
    
    r = requests.post('https://gql.twitch.tv/gql', headers=_header, json=_json)

    return json.loads(r.text)['data']['user']['lastBroadcast']['title']

def get_stream():
    _header = {
        'Client-Id':'kimne78kx3ncx6brgo4mv6wki5h1ko'
    }

    _json = {
        "operationNam":"StreamMetadata",
        "extensions":{
            "persistedQuery":{
                "version":1,
                "sha256Hash":"a647c2a13599e5991e175155f798ca7f1ecddde73f7f341f39009c14dbf59962"
            }
        },
        "variables":{
            "channelLogin":"steelohs"
        }
    }
    
    r = requests.post('https://gql.twitch.tv/gql', headers=_header, json=_json)

    return json.loads(r.text)['data']['user']['stream']