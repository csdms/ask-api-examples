"""Queries the CSDMS model repository for all models written in C."""
from ask_api_examples import make_query


query = '[[Programming language::C]]|limit=10000'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
