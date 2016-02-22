"""Queries the CSDMS model repository for C models written by user 'Tucker'."""
from csdms_wiki_api_examples import make_query


query = '[[Programming language::C]][[Last name::Tucker]]'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
