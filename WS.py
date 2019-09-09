import requests

host = 'http://localhost:8080/'

def GET(url):
    r = requests.get(host + url)
    return r

def POST(url, data):
    requests.post(host + url, data)