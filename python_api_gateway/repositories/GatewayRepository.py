import http.client
import json

headers = {
    'Content-type': 'application/json'
}

class PersonsRepository(object):
    def gateway(self, data, url):

        json_data_post = json.dumps(data)

        if 'users' in url:
            conn = http.client.HTTPConnection("localhost:5010")
    
            if 'create' not in url:

                conn.request("POST", "/users/login", json_data_post, headers=headers)
                res = conn.getresponse()
                data = res.read()

                data_json = json.loads(data.decode("utf-8"))
                jwt_token = data_json['token']

                new_headers = {
                    'Content-type': 'application/json',
                    'authorization': jwt_token
                }
                if 'friendRequestId' in url or 'send-friend-request' in url:
                    conn.request('POST', url, headers=new_headers)
                else:
                    conn.request('GET', url, headers=new_headers)
            else:
                conn.request("POST", url, json_data_post, headers=headers)

        elif 'persons' in url:
            conn = http.client.HTTPConnection("localhost:5000") 
            if 'delete' in url or 'person1' in url:
                conn.request('POST', url, headers=headers)
            else:
                conn.request('GET', url, headers=headers)

        elif 'publications' in url:

            conn = http.client.HTTPConnection("localhost:5020")
            conn.request("POST", "/users/login", json_data_post, headers=headers)
            res = conn.getresponse()
            data = res.read()

            data_json = json.loads(data.decode("utf-8"))
            jwt_token = data_json['token']

            new_headers = {
                'Content-type': 'application/json',
                'authorization': jwt_token
            }

            if 'friends' in url or 'mypubs' in url:
                conn.request('GET', url, headers=new_headers)
            else:
                conn.request('POST', url, headers=new_headers)


            

