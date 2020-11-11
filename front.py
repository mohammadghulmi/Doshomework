import requests
catalog=" http://127.0.0.1:4000/"
order=" http://127.0.0.1:5000/"
def buy(id):
    response=requests.post(order+"buy/"+id)
    print(response.json())
def search(topic):
    res=requests.get(catalog+"search/"+topic)
    print(res.json())
def lookup(id):
    res=requests.get(catalog+"lookup/"+id)
    print(res.json())
while True:
    val =input("enter s to search l to lookup b to buy")
    if val == "b":
            while True:
                val = input("enter the product number")
                if val.isdecimal():
                    buy(val)
                    break
                else: print("enter a number")
    elif val =="l" :
            while True:
                val = input("enter the product number")
                if val.isdecimal():
                    lookup(val)
                    break
                else: print("enter a number")
    elif val =="s":
            val = input("enter a topic")
            search(val)
    else:
        print("enter a valid input")

