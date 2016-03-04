"""Queries the CSDMS model repository for all models written in C,
C++, Fortran 77, or Fortran 90."""
from ask_api_examples import make_query


query = '[[Programming language::C||C++||Fortran77||Fortran90]]|limit=10000'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
