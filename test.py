import requests
#f = open("data.txt", "w")
#books = [["How-to-get-a-good-grade-in-DOS-in-20-minutes-a-day" , "distributed systems" , "20" , "7","1"],["RPCs for Dummies","distributed systems","25","4","2"],["Xen and the Art of Surviving Graduate School","graduate school","10","8", "3"],["Cooking for the Impatient Graduate Student","graduate school","40","3", "4"]]

#for i in range(4):
 #for j in range(5):
    # f.write(books[i][j]+"\n")
Base=" http://127.0.0.1:5000/"
response= requests.post(Base+"buy/2")
print("request is post")
print(response.json())