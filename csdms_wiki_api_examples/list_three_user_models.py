"""Queries the CSDMS model repository for three models written by user
'Tucker'."""
from csdms_wiki_api_examples import make_query


query = '[[Last name::Tucker]]|limit=3'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
