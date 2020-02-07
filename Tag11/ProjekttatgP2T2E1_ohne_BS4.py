import requests
from bs4 import BeautifulSoup


baserurl="https://www.twitter.com/"
handle = input("Twitter handle: @")
request = requests.get(baserurl+handle)

reqtext = request.text

findex = reqtext.index("followers_count&quot;:") + 22
endindex = reqtext.index(",&quot",findex+22)
fcountstring = reqtext[findex:endindex]

print(f"@{handle} has {fcountstring} followers.")

# soup = BS(request.text,"html.parser")
# print