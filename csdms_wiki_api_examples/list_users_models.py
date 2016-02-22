"""An example of querying the CSDMS model repository for models written
by the user with the last name 'Tucker'.
"""
import os
from csdms_wiki_api_examples import call_api, write_file


def main():
    query = '[[Last name::Tucker]]'
    r = call_api(query)
    base_file_name, ext = os.path.splitext(__file__)
    write_file(r, base_file_name)
    print r


if __name__ == '__main__':
    main()
