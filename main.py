import requests
import threading
        
print("""
###########################################
####### @Author - MR.Arijit Paine #########
###########################################
""")
        
url = input("Url:- ")
requestNumber = int(input("Number of requests:- "))
        
def getRequest(num):
    print(num,requests.get(url))
        
a = 0
while 1:
    a += 1
    t = threading.Thread(target=getRequest,args=(a,))
    t.start()
    if a == requestNumber:
        break
        
#https://m.youtube.com/f9b57bf6-1239-42ca-9960-80c378d93b0a