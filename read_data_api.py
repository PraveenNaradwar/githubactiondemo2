import requests
import pandas as pd
import os

token=os.getenv("API_TOKEN")
print(f" Token : {token}")

if token=="1234":
    print("correct")
else:
    print("incorrect")    

response=requests.get("https://jsonplaceholder.typicode.com/users")
data=response.json()

df=pd.DataFrame(data)
df=df[["id","name"]]
print(df)