import json
from bs4 import BeautifulSoup

url = "/Users/lionars/00_neurips/output_udf.html"
soup = BeautifulSoup(open(url))
text = soup.get_text()

#x
start = text.find('\"x\"')
end = text[start:].find("]")
end+= start
x = "{" + text[start:end+1] + "}"
x_json = json.loads(x)
print(len(x_json['x']))

#y
start = text.find('\"y\"')
end = text[start:].find("]")
end+= start
y = "{" + text[start:end+1] + "}"
y_json = json.loads(y)
print(len(y_json['y']))

#z
start = text.find('\"z\"')
end = text[start:].find("]")
end+= start
z = "{" + text[start:end+1] + "}"
z_json = json.loads(z)
print(len(z_json['z']))

#color
start = text.find('\"color\"')
end = text[start:].find("]")
end+= start
c = "{" + text[start:end+1] + "}"
c_json = json.loads(c)
print(len(c_json['color']))

dictionary = {}
dictionary['x'] = x_json['x']
dictionary['y'] = y_json['y']
dictionary['z'] = z_json['z']
dictionary['color'] = c_json['color']

with open("pointcloud.json", "w") as outfile:
    json.dump(dictionary, outfile)



