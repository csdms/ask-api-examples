"""Lists a category of models from the CSDMS model metadata repository."""
from ask_api_examples import make_query


query = '[[Category:Terrestrial||Coastal||Marine||Hydrology||Carbonate||Climate]]|limit=10000'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
