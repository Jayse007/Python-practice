import request_tutorial


res = request_tutorial.get('https://automatetheboringstuff.com/files/rj.txt')
 
print(res.status_code)

if res.raise_for_status():
    print("An error occurred")

else:
    print("Request successful")