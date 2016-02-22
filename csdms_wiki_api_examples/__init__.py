"""Examples of using the Semantic MediaWiki Ask API to query the
CSDMS model metadata repository.
"""
import os
import urllib


base_url = 'http://csdms.colorado.edu/mediawiki/api.php?'
params = {'action': 'ask', 'format': 'json'}


def call_api(query='[[Model:HydroTrend]]'):
    params['query'] = query
    fp = urllib.urlopen(base_url, urllib.urlencode(params))
    return fp.read()


def write_file(json_str, base_file_name):
    with open(base_file_name + '.json', 'w') as fp:
        fp.write(json_str)


def make_query(query, file_name):
    r = call_api(query)
    base_file_name, ext = os.path.splitext(file_name)
    write_file(r, base_file_name)
    return r
