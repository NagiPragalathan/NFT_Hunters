
import json

person_dict = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open('C:/Users/NagiPragalathan/Desktop/NFT_Hunters/NFT_Craft/datas.json', 'w') as json_file:
  json.dump(person_dict, json_file)


with open('C:/Users/NagiPragalathan/Desktop/NFT_Hunters/NFT_Craft/datas.json', 'r') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'French']}
print(data)

# https://github.com/kairess/minecraft-clone.git