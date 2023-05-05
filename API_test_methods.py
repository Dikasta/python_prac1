import json

import requests
getvar= 'https://api.openweathermap.org/data/2.5/weather'
postvar = "https://jsonplaceholder.typicode.com/todos"
putvar= 'https://api.github.com/some/endpoint'

# getmethod implemetation
req= requests.get(getvar)
data= req.json()
print(data)

#implement post
data1 = {
        'api_option':'paste',
        'api_paste_code':123,
        'api_paste_format':'python'}
req=requests.post(postvar,data=data1)
print(req.json())  #op ={'api_option': 'paste', 'api_paste_code': '123', 'api_paste_format': 'python', 'id': 201}

# implement put
payload = {'some': 'data'}
headers = {"content-type": "application/json", "Authorization": "<auth-key>" }
req= requests.put(putvar,data=json.dumps(payload),headers=headers)
print(req.headers)
print(req.status_code) #404
print(req.content)  #b'{"message":"Not Found","documentation_url":"https://docs.github.com/rest"}'

#o/p {'Server': 'GitHub.com', 'Date': 'Fri, 05 May 2023 02:10:18 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'X-GitHub-Media-Type': 'github.v3; format=json', 'x-github-api-version-selected': '2022-11-28', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '58', 'X-RateLimit-Reset': '1683255887', 'X-RateLimit-Used': '2', 'X-RateLimit-Resource': 'core', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, X-GitHub-SSO, X-GitHub-Request-Id, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Vary': 'Accept-Encoding, Accept, X-Requested-With', 'Content-Encoding': 'gzip', 'X-GitHub-Request-Id': 'C707:668D:404493:4627A5:6454658A'}


# implement delete
x = requests.delete('https://w3schools.com/python/demopage.php')
#print(x.status_code)
print(x.content)  #b'' -----------recored deleted



#dfdgjh