"""List five models written in C, starting at item 20 from the full
list.
"""
from csdms_wiki_api_examples import make_query


query = '[[Programming language::Python]]|limit=5|offset=20'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
