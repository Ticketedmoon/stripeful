import requests

def main():
    r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
    status_code = r.status_code
    headers = r.headers['content-type']
    encoding = r.encoding
    test = r.text
    jsonBody = r.json()
    print(jsonBody)

if __name__ == "__main__":
    main()
