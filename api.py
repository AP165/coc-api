import requests

my_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjlmYzYyYjc3LTI5ZTYtNGMyOS05MmIwLTkwMWY5Njg3MWZlYiIsImlhdCI6MTYxNzQ1NzUzNCwic3ViIjoiZGV2ZWxvcGVyL2I1MTQwMmY3LTIxMGMtMDgxZS02MGQyLTQ0M2ZhOWY1MGUxNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjM0LjIyOC4zMi4xODgiXSwidHlwZSI6ImNsaWVudCJ9XX0.AD65XKH62PEiaWF1xsrx6VgqK7cdR-1plvSow9SzTZnP1yFNCTnWP7NdnexvcM_N-bLiY6tG8Qydp4i1Z80Kxg"

url = "https://api.clashofclans.com/v1/clans/ JCJL2CYG"
headers = {
        'Accept': "application/json",
        'authorization': "Bearer %s" % my_key
}
response = requests.request("GET", url, headers=headers )
data = response.json()
print(data)
