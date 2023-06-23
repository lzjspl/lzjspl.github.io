import json
fn = "/Users/lionars/01_projects/intractablecat.github.io/static/resources/iphone/chair/pointcloud.json"
f = open(fn)
data = json.load(f)


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

#xaxis range
start = text.find('\"xaxis\":{\"range\"')
end = text[start:].find("]")
end+= start
xaxis = "{" + text[start:end+1] + "}}"
xaxis_json = json.loads(xaxis)
xaxis_range = xaxis_json['xaxis']['range']
print(xaxis_range)

#yaxis range
start = text.find('\"yaxis\":{\"range\"')
end = text[start:].find("]")
end+= start
yaxis = "{" + text[start:end+1] + "}}"
yaxis_json = json.loads(yaxis)
yaxis_range = yaxis_json['yaxis']['range']
print(yaxis_range)

#zaxis range
start = text.find('\"zaxis\":{\"range\"')
end = text[start:].find("]")
end+= start
zaxis = "{" + text[start:end+1] + "}}"
zaxis_json = json.loads(zaxis)
zaxis_range = zaxis_json['zaxis']['range']
print(zaxis_range)


dictionary = {}
dictionary['x'] = x_json['x']
dictionary['y'] = y_json['y']
dictionary['z'] = z_json['z']
dictionary['color'] = c_json['color']

dictionary = {}
dictionary['x'] = x_json['x']
dictionary['y'] = y_json['y']
dictionary['z'] = z_json['z']
dictionary['color'] = c_json['color']
dictionary['xaxis_range'] = xaxis_range
dictionary['yaxis_range'] = yaxis_range
dictionary['zaxis_range'] = zaxis_range

with open("pointcloud.json", "w") as outfile:
    json.dump(dictionary, outfile)



