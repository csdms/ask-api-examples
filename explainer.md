# Querying the CSDMS Website

The [CSDMS portal](http://csdms.colorado.edu/wiki/Main_Page) uses
[Semantic MediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) (SMW)
to store and query information.
SMW has an [API](https://www.semantic-mediawiki.org/w/api.php) with several actions.
Here, we'll focus on the `ask` action,
and the [Ask API](https://www.semantic-mediawiki.org/wiki/Ask_API),
to query metadata from the CSDMS model repository.

The base URL for any call to the SMW API on the CSDMS portal is
http://csdms.colorado.edu/mediawiki/api.php.


## Basic queries

The `ask` action supports one parameter, `query`,
which takes an urlencoded string.
The query is written in the SMW query language.
A query consists of a series of *conditions*,
which describe the search.
Conditions are built from *properties* and *values*.
For example, the condition
```
[[Programming language::C]]
```
would query for all models with the `Programming language` property
that have a value of `C`.
Note that the brackets `[]` and the colons `::` in the condition
are literal in the query language,
and cannot be urlencoded.
Spaces, however, should be encoded with `%20` or `+`.

Try this condition in a query:
* [http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&format=json](http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&format=json)

The results of a query are returned as JSON
with a specified
[format](https://www.semantic-mediawiki.org/wiki/Serialization_%28JSON%29).
A query result can also be viewed in pretty print form 
by removing the `format` parameter from the query.


## Examples of queries

Here are some examples of queries into the CSDMS model repository.

| Description | Query URL |
|-------------|-----------|
| List all models created by the user with the last name `Tucker` | [http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&format=json](http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&format=json) |
| List all models from user `Tucker` written in `C` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming%20language::C]]&format=json |
| List models written by user `Tucker`, including the model DOI in the results | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&#124;?DOI+model&format=json |
| List the first five models written by user `Tucker` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&#124;?limit=5&format=json |
| List five models written in `C`, starting at item 10 from the full list | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&#124;?DOI+model&#124;limit=5&#124;offset=10 |
| Search for a nonexistent `Programming language` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::xxyyzz]]&format=jsonfm |