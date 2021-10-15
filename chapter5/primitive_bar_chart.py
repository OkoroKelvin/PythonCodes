from urllib import request

r = request.urlopen("https://www.google.com")
print(r.getcode())
print(r.read())