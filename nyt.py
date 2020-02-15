import requests
import json
key = "removed key before upload to github"
url = "https://api.nytimes.com/svc/archive/v1/2019/12.json?&api-key="+key
r=requests.get(url)
json_data= r.json()
ofile=open("data.txt","w")
#print(json_data)

for i in range(5000):
    try:
        ofile.write("'"+json_data["response"]["docs"][i]["headline"]["main"]+"','"+json_data["response"]["docs"][i]["lead_paragraph"]+"',"+"REAL\n")
    except IndexError:
        print(i)
        exit(0)
"""
print(json_data["response"]["docs"][5]["lead_paragraph"])
"""
"""
with open('data.txt', 'w') as outfile:
    json.dump(json_data,outfile,ensure_ascii=False, indent=4)
"""
#ofile.close()
