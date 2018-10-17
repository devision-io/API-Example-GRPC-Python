from metasdk.apiclient import ApiClient

api = ApiClient.build_from_developer_settings("example", "v2")
api.host = "http://localhost:8083"

resp = api.post("currency-rates/get", post_data={
    "date": "2018-10-01"
})

print(u"resp = %s" % str(resp))
