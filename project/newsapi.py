import requests
import json

class Query(object): # pylint: disable=too-few-public-methods
	pass



def getNewsQuery(keyword, source):
    url = ('https://newsapi.org/v2/everything?'
       'q=' + keyword + '&'
       'sources=' + source + '&'
       #'sortBy=popularity&'
       'apiKey=' + '8661aeb44b0c45b29962447873da64db')
    response = requests.get(url)
    parsed = json.loads(json.dumps(response.json()))
    print(json.dumps(parsed, indent=4, sort_keys=True))

sources = "cnn, buzzfeed, the-new-york-times"

print("apple\n\n")
getNewsQuery("Apple", sources)
print("don\n\n")
getNewsQuery("Donald Trump", sources)
print("go blue\n\n")
getNewsQuery("University of Michigan", sources)
print("Duo\n\n")
getNewsQuery("Duo", sources)