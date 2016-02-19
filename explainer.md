# Querying the CSDMS Website

The [CSDMS portal](http://csdms.colorado.edu/wiki/Main_Page) uses
[Semantic MediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) (SMW)
to store and query information.
SMW has an [API](https://www.semantic-mediawiki.org/w/api.php) with several actions.
Here, we'll focus on the `ask` action,
and the [Ask API](https://www.semantic-mediawiki.org/wiki/Ask_API),
to query metadata from the CSDMS model metadata repository.

The base URL for any call to the SMW API on the CSDMS portal is
http://csdms.colorado.edu/mediawiki/api.php.


## Query syntax

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


## Categories

[Categories](https://www.semantic-mediawiki.org/wiki/Help:Editing) 
are tags added to a page
to aid in classification.
Like properties,
categories can be queried.
For example,
the condition
```
[[Category:Terrestrial]]
```
will list all terrestrial models the CSDMS model metadata repository.
Unlike properties,
only one colon `:` separates the category name and value.

`Model` is itself a category in the CSDMS wiki.
Search for a particular model by name:
```
[[Model:HydroTrend]]
```
The category value is case-sensitive;
e.g., `hydrotrend` wouldn't match a model.
Here's this condition in a query:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Model:HydroTrend]]&format=json


## Advanced queries

Conditions listed in serial are combined with a logical `AND`.
For example,
the two conditions
```
[[Programming language::C++]]
[[Last name::Tucker]]
```
can be combined into a query like so:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C%2B%2B]][[Last+name::Tucker]]&format=jsonfm

Note that spaces in the properties need to be urlencoded
(here, with `+`),
as well as the plus signs in `C++`
(here, with `%2B`)!


## Model keywords

Model keywords are defined not by SMW,
but by the developer of the model,
so they may be inconsistent,
and vary from model to model.
For example, the condition
```
[[Model keywords::basin]]
```
can be used to find all models that have the keyword `basin`.
Use this condition in a query:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Model+keywords::basin]]&format=jsonfm


## Testing queries

Test queries with the `Special:Ask` page on the CSDMS portal:
http://csdms.colorado.edu/wiki/Special:Ask.
In addition to interactively running queries,
the `Special:Ask` page shows the raw query string,
which can be helpful for building new queries programmatically.


## Examples of queries

Here are some examples of queries into the CSDMS model repository.

| Description | Query URL |
|-------------|-----------|
| List all models created by the user with the last name `Tucker` | [http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&format=json](http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&format=json) |
| List all models written in `C` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming%20language::C]]&format=json |
| List all models from user `Tucker` written in `C` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]][[Programming%20language::C]]&format=json |
| List models written by user `Tucker`, including the model DOI in the results | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&#124;?DOI+model&format=json |
| List the first five models written by user `Tucker` | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&#124;?limit=5&format=json |
| List five models written in `C`, starting at item 10 from the full list | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&#124;?DOI+model&#124;limit=5&#124;offset=10 |
| Search for models written a nonexistent programming language to see an error message | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::xxyyzz]]&format=jsonfm |
| Find all terrestrial models | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Category:Terrestrial]]&format=jsonfm |
| Locate a particular model by name | http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Model:HydroTrend]]&format=json |


## Additional references

* Properties: https://www.semantic-mediawiki.org/wiki/Help:Properties_and_types
* Results formats: https://www.semantic-mediawiki.org/wiki/Help:Result_formats
