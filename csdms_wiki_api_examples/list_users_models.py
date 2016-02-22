"""Queries the CSDMS model repository for models written by the user
with the last name 'Tucker'.
"""
from csdms_wiki_api_examples import make_query


query = '[[Last name::Tucker]]'


def main():
    r = make_query(query, __file__)
    print r


if __name__ == '__main__':
    main()
