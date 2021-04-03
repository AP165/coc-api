from flask import Flask, render_template,request
import requests

app = Flask(__name__)

my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg5NzFjMTQ3LTAzNDEtNDY0My04ZjAxLWQzMmFlOWY5YTllMiIsImlhdCI6MTYxNjkzMjMyOCwic3ViIjoiZGV2ZWxvcGVyL2I1MTQwMmY3LTIxMGMtMDgxZS02MGQyLTQ0M2ZhOWY1MGUxNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExNy4yMjcuNjMuNTAiLCIxMTcuMjI3LjgyLjI1Il0sInR5cGUiOiJjbGllbnQifV19.6molpH5u5B6t1en5npnjcjDKcZTQQtMjNp5lf_9KFso0YgC5FGmgJJzA1KcdNuOhT00bRXgZOM0Wo3YXgU7MSA"

@app.route("/")
def hello():
    url = "https://api.clashofclans.com/v1/locations"
    headers = {
        'Accept': "application/json",
        'authorization': "Bearer %s" % my_key
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(data)


    return render_template("index.html", data = data)

@app.route("/clan",methods = ['GET','POST'])
def info():
    print(request.form)
    clanTag = request.form['clanTag']
    
    try:
        warFrequency = "&warFrequency="+request.form['warFrequency']
    except Exception as e:
        warFrequency = ""
    
    try:
        location = "&locationId="+request.form['location']
    except Exception as e:
        location = ""
    
    try:
        minClanMembers = "&minMembers="+request.form['minClanMembers']
    except Exception as e:
        minClanMembers = ""
        
    try:
        maxClanMembers = "&maxMembers="+request.form['maxClanMembers']
    except Exception as e:
        maxClanMembers = ""
        
    try:
        minClanPoints = "&minClanPoints="+request.form['ClanScore']
    except Exception as e:
        minClanPoints = ""
    
    try:
        minClanLevel = "&minClanLevel="+request.form['minClanLevel']
    except Exception as e:
        minClanLevel = ""
    
    url = "https://api.clashofclans.com/v1/clans?name="+clanTag+warFrequency+location+minClanMembers+maxClanMembers+minClanPoints+minClanLevel
    
    headers = {
        'Accept': "application/json",
        'authorization': "Bearer %s" % my_key
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    #print(data)
    return render_template("info.html",data = data,clanTag = clanTag)
    #return data

@app.route("/clan/info",methods = ['GET','POST'])
def clan():
    ctag = request.form['clanTag']
    try:
        ctag2 = ctag.replace("#"," ")
    except Exception as e:
        ctag2 = " "+ctag
    url = "https://api.clashofclans.com/v1/clans/"+ctag2
    headers = {
            'Accept': "application/json",
            'authorization': "Bearer %s" % my_key
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(url)
    return render_template("clans.html",data = data)
    #return data
    
@app.route("/clan/info/member" , methods = ['GET', 'POST'])
def ClanMemberInfo():
    memberTag = request.form["memberTag"]
    memberTag2 = memberTag.replace("#"," ")

    url = "https://api.clashofclans.com/v1/players/"+memberTag2
    headers = {
            'Accept': "application/json",
            'authorization': "Bearer %s" % my_key
    }
    response = requests.request("GET", url, headers=headers)
    data = response.json()
    print(memberTag2,"\n")
    
    
    
    # return data
    return render_template("clanMember.html", data = data)


    #________errorhandlers_________#
@app.errorhandler(404)
def invalid_route(e): 
    return e

@app.errorhandler(500)
def internal_error(error):
    return """<!DOCTYPE html><html><head><meta><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><style type="text/css" media="all">body{ padding: 1rem 2rem; }</style><title>500</title></head><body><pre><code style="font-size: 0.8rem;line-height: 25px">{<br>    <span style="color: green; font-weight: bold;">"errorCode" </span>: <span style="color: #820bff;"><strong>404</strong></span>,<br>    <span style="color: green; font-weight: bold;">"reason" </span>: <span style="color: blue;">"invalidTag"</span>,<br>    <span style="color: green; font-weight: bold;">"massage" </span>: <span style="color: blue;">"Invalid ClanTag: Enter a valid ClanTag"</span><br>}</code></pre></body></html>"""
app.run(debug=False,host="0.0.0.0")
