import requests

from urllib.parse import urlparse

def parse_urlhaus(url):
    data = []
    columns = ['id','dateadded','url','url_status','threat','tags','urlhaus_link', 'domain']
    r = requests.get(url).text.split('\n')
    for line in r:
        if not line.startswith('#'):
            data.append(line.strip('\n'))
    csv_data = csv.DictReader(data, delimiter=',', quotechar='"', escapechar='\\', fieldnames=columns)
    return csv_data

urlhaus = 'https://urlhaus.abuse.ch/downloads/csv/'
parsed_urlhaus = list(parse_urlhaus(urlhaus))
# Get domains
for d in parsed_urlhaus:
    d['domain'] = urlparse(d['url']).netloc
