import requests
from bs4 import BeautifulSoup

handle = '@elonmusk'

handle = handle[1:]

url = 'https://twitter.com/'

r = requests.get(url+handle)

soup = BeautifulSoup(r.text, 'html.parser')

# soup_follow = soup.find(
#     'a', {
#         'class':
#         'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor'
#     })
#
# soup_follow = soup_follow.find_next('a', {'class': 'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor'
#     })

soup_follow = soup.find('a', {'data-nav':"followers"})

print(soup_follow['title'])
