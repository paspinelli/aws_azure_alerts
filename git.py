import requests
url = "curl -H "Authorization: token " https://api.github.com/orgs/"
#url1 ="curl -H "Authorization: token " https://api.github.com/orgs/ | grep login >> github.txt " 
#url2 ="curl -H "Authorization: token " https://api.github.com/orgs/ | grep login >> github.txt"
#url3 ="curl -H "Authorization: token " https://api.github.com/orgs/| grep login >> github.txt"
#url5 ="curl -H "Authorization: token " https://api.github.com/orgs/| grep login >> github.txt"
data = requests.get(url).json
print url
