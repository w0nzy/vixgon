import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbHBlcmVuIiwiZXhwIjoxODI4MTE3MTg1fQ.pOpYuoyfM9eX1cVVoxzerwHCiOl9w-bZsfZc64f3_eU"

resp = requests.get("http://127.0.0.1/vixgon/api/get_shelfs",headers={"Authorization":"Bearer %s" % (token)})
print(resp.headers)