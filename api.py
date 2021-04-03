import requests

my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg5NzFjMTQ3LTAzNDEtNDY0My04ZjAxLWQzMmFlOWY5YTllMiIsImlhdCI6MTYxNjkzMjMyOCwic3ViIjoiZGV2ZWxvcGVyL2I1MTQwMmY3LTIxMGMtMDgxZS02MGQyLTQ0M2ZhOWY1MGUxNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExNy4yMjcuNjMuNTAiLCIxMTcuMjI3LjgyLjI1Il0sInR5cGUiOiJjbGllbnQifV19.6molpH5u5B6t1en5npnjcjDKcZTQQtMjNp5lf_9KFso0YgC5FGmgJJzA1KcdNuOhT00bRXgZOM0Wo3YXgU7MSA"

url = "https://api.clashofclans.com/v1/clans/ JCJL2CYG"
headers = {
        'Accept': "application/json",
        'authorization': "Bearer %s" % my_key
}
response = requests.request("GET", url, headers=headers )
data = response.json()
print(data)