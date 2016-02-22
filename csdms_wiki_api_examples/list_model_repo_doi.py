"""Find all models written by user Hutton, including the DOI and the
source code repository for each model.

"""
from csdms_wiki_api_examples import make_query


query = '[[Last name::Hutton]]|?DOI model|?Source web address'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
