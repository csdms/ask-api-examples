"""Queries the CSDMS model repository for models written by the user
with the last name 'Tucker'.
"""
from ask_api_examples import make_query


query = '[[Last name::Tucker]]'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
