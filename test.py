import requests

r = requests.get('http://127.0.0.1:8000/api/posts/')

posts = eval(r.text) 
for i in posts:
    print(f"""{i['description']}\n{i['image_or_video']}""")