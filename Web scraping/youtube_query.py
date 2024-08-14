import requests



query = input("What do you want to search on Youtube")



rest = requests.get("https://www.youtube.com/", params= {'search_query': query})

rest.raise_for_status()
print(rest.text)