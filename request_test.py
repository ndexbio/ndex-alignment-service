from networkn import NdexGraph
import requests
import json

primary = NdexGraph(server='http://public.ndexbio.org', uuid='4a5bc352-9243-11e5-b435-06603eb7f303')
secondary = NdexGraph(server='http://public.ndexbio.org', uuid='19f2fc35-1235-11e6-a039-06603eb7f303')

primary.show_stats()
secondary.show_stats()

payload = {'primary': primary.to_cx(), 'secondary': secondary.to_cx()}

r = requests.post('http://0.0.0.0:8080/expand', data=json.dumps(payload))

# with open('request.json', 'w') as outfile:
#     json.dump(r.json(), outfile)


result = NdexGraph(r.json())

result.show_stats()