"""Examples of using the Semantic MediaWiki Ask API to query the
CSDMS model metadata repository.
"""
import urllib


base_url = 'http://csdms.colorado.edu/mediawiki/api.php?'
params = {'action': 'ask', 'format': 'json'}


def call_api(query='[[Model:HydroTrend]]'):
    params['query'] = query
    fp = urllib.urlopen(base_url, urllib.urlencode(params))
    return fp.read()


def write_file(json_str, file_name):
    with open(file_name + '.json', 'w') as fp:
        fp.write(json_str)
