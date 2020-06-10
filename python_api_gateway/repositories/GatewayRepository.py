import http.client

headers = {
    'Content-type': 'application/json'
}

class PersonsRepository(object):
    def gateway(self, url):
        if 'users' in url:
        elif 'persons' in url:
            conn = http.client.HTTPConnection("localhost:5000") 
            if 'delete' in url or 'person1' in url:
                conn.request('POST', url, headers=headers)
            else:
                conn_.request('GET', url, headers=headers)
        elif 'publications' in url: