import requests
url = 'https://www.globo.com/'
page = requests.get(url)
page.content
