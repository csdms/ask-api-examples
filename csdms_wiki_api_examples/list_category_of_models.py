"""Lists a category of models from the CSDMS model metadata repository."""
from csdms_wiki_api_examples import make_query


query = '[[Category:Terrestrial]]|limit=10000'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
