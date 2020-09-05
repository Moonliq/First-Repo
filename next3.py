msk = {'city': "Moscow", "temperature": "20"}
print(msk['city'])
n = int(msk['temperature']) - 5
print(n)
msk['temperature'] = str(n)
print(msk)
print(msk.get('country'))
msk["country"] = 'Russia'
print(msk)
print(len(msk))