"""Query for a nonexistent language to see the resulting error message."""
from ask_api_examples import make_query


query = '[[Programming language::xxyyzz]]'


def main():
    r = make_query(query, __file__)
    return r


if __name__ == '__main__':
    print main()
