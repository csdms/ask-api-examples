"""Locate a model by name using the Model category."""
from csdms_wiki_api_examples import make_query


query = '[[Model:HydroTrend]]'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
