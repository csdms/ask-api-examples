# Querying the CSDMS Website

[Semantic MediaWiki](https://www.semantic-mediawiki.org/wiki/Semantic_MediaWiki) (SMW)
is the knowledge management system used on the
[CSDMS website](http://csdms.colorado.edu/wiki/Main_Page).
SMW has an [API](https://www.semantic-mediawiki.org/w/api.php)
with several actions, allowing users
to add, edit, and query information.
Here, we'll focus on the `ask` action,
and the [Ask API](https://www.semantic-mediawiki.org/wiki/Ask_API),
to query metadata from the CSDMS model metadata repository.

The base URL for any call to the SMW API on the CSDMS website is
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
Note that the colons `::` in the condition
are literal in the query language,
and cannot be urlencoded.
Spaces, however, should be encoded with `%20` or `+`,
while brackets `[]` may optionally be encoded.

Try this condition in a query:
* [http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&format=json](http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]&format=json)

The results of a query are returned as JSON
with a specified
[format](https://www.semantic-mediawiki.org/wiki/Serialization_%28JSON%29).
A query result can also be viewed in pretty print form 
by removing the `format` parameter from the query.


## Properties

[Properties](https://www.semantic-mediawiki.org/wiki/Help:Properties_and_types)
are the basic data type of SMW.
They consist of a name and a value,
both of which are case-sensitive.

A defined set of properties are added to each model
by the CSDMS WikiSysop.
For example,
`Programming language` is a property of models
in the CSDMS model metadata repository.

**Note:**
I desire a query that returns all the properties of a model,
but I haven't figured out how to make it.
It's on my list of unanswered questions below.
In lieu of a programmatic query,
I've been looking at the model's wiki source;
for example, the
[Wikitext for HydroTrend](http://csdms.colorado.edu/mediawiki/index.php?title=Model:HydroTrend&action=edit).


## Categories

[Categories](https://www.semantic-mediawiki.org/wiki/Help:Editing) 
are tags added to a page
by the CSDMS WikiSysop
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


## Model keywords

Model keywords are defined not by SMW or the CSDMS WikiSysop,
but by the developer of a model,
so they may inconsistently
vary from model to model.
For example, the condition
```
[[Model keywords::basin]]
```
can be used to find all models that contain the keyword `basin`.
Use this condition in a query:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Model+keywords::basin]]&format=jsonfm


## Advanced queries

The Ask API supports a number of advanced query options.

### Limiting the displayed results

By default,
only the first 10 matches to a query are returned.
To raise this limit,
set the `limit` display property to a larger number.
For example, in applying this to the example above
```
[[Programming language::C]]|limit=10000
```
we see that there are (at the time of writing this article)
actually 100 models written in C.
Note the use of the pipe character `|` to set off
the display property from the condition.
Here's the query:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::C]]|limit=10000&format=jsonfm


### Combining conditions

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

Conditions can support multiple values
combined with a logical `OR` operation using the double pipe `||` operator.
For example,
to list models written in either Fortran 77 or Fortran 90,
use the condition
```
[[Programming language::Fortran77||Fortran90]]
```
in a query this is:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming+language::Fortran77||Fortran90]]|limit=10000&format=jsonfm


See [Help:Selecting_pages](https://www.semantic-mediawiki.org/wiki/Help:Selecting_pages)
for examples of disjunctions and comparisons of conditionals.


### Specifying additional data

Additional data can be returned with a query result
by specifying additional properties in query string.
Separate additional properties with the pipe and question mark characters `|?`.
For example,
to find all models written by the user with the last name "Hutton",
and also include, if available,
the DOI and the source code repository for each model found,
use the query string:
```
[[Last+name::Hutton]]|?DOI+model|?Source+web+address
```
The API call:

* http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Hutton]]|?DOI+model|?Source+web+address&format=jsonfm

See [Help:Inline_queries](https://www.semantic-mediawiki.org/wiki/Help:Inline_queries)
for more information on building query strings with several properties.


## Testing queries

Test queries with the `Special:Ask` page on the CSDMS portal:
http://csdms.colorado.edu/wiki/Special:Ask.
In addition to interactively running queries,
the `Special:Ask` page shows the raw query string,
which can be helpful for building new queries programmatically.


## Examples of queries

Here are some examples of queries into the CSDMS model repository.

<table><thead>
<tr>
<th>Description</th>
<th>Query URL</th>
</tr>
</thead><tbody>
<tr>
<td>List all models created by the user with the last name Tucker</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BLast+name::Tucker%5D%5D&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Last+name::Tucker]]&format=json</a></td>
</tr>
<tr>
<td>List all models written in C</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BProgramming%20language::C%5D%5D&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming%20language::C]]&format=json</a></td>
</tr>
<tr>
<td>Really list all models written in C</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BProgramming%20language::C%5D%5D&#124;limit=10000&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming%20language::C]]|limit=10000&format=json</a></td>
</tr>
<tr>
<td>List all models from user Tucker written in C</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BLast+name::Tucker%5D%5D%5B%5BProgramming%20language::C%5D%5D&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Last+name::Tucker]][[Programming%20language::C]]&amp;format=json</a></td>
</tr>
<tr>
<td>List the first three models written by user Tucker</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BLast+name::Tucker%5D%5D&#124;limit=3&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Last+name::Tucker]]|limit=3&amp;format=json</a></td>
</tr>
<tr>
<td>List five models written in C, starting at item 20 from the full list</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BProgramming+language::C%5D%5D&#124;limit=5&#124;offset=20">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Programming+language::C]]|limit=5|offset=20</a></td>
</tr>
<tr>
<td>Search for models written a nonexistent programming language to see an error message</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BProgramming+language::xxyyzz%5D%5D&amp;format=jsonfm">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Programming+language::xxyyzz]]&amp;format=jsonfm</a></td>
</tr>
<tr>
<td>Find all terrestrial models</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BCategory:Terrestrial%5D%5D&amp;format=jsonfm">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Category:Terrestrial]]&amp;format=jsonfm</a></td>
</tr>
<tr>
<td>Locate a particular model by name</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BModel:HydroTrend%5D%5D&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Model:HydroTrend]]&amp;format=json</a></td>
</tr>
<tr>
<td>List all models written in Fortran 77 or Fortran 90</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BProgramming%20language::Fortran77&#124;&#124;Fortran90%5D%5D&#124;limit=10000&amp;format=json">http://csdms.colorado.edu/mediawiki/api.php?action=ask&query=[[Programming%20language::Fortran77||Fortran90]]|limit=10000&format=json</a></td>
</tr>
<tr>
<td>Find all models written by user Hutton, including (if available) the DOI and the source code repository for each model</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BLast+name::Hutton%5D%5D&#124;?DOI+model&#124;?Source+web+address&amp;format=jsonfm">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Last+name::Hutton]]&#124;?DOI+model&#124;?Source+web+address&format=jsonfm</a></td>
</tr>
<tr>
<td>List all models (Category technique)</td>
<td><a href="http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=%5B%5BCategory:Terrestrial||Coastal||Marine||Hydrology||Carbonate||Climate%5D%5D&#124;limit=10000&amp;format=jsonfm">http://csdms.colorado.edu/mediawiki/api.php?action=ask&amp;query=[[Category:Terrestrial&#124;&#124;Coastal&#124;&#124;Marine&#124;&#124;Hydrology&#124;&#124;Carbonate&#124;&#124;Climate]]|limit=10000&amp;format=jsonfm</a></td>
</tr>
</tbody></table>


## Unanswered questions

1. How does one get a list of all model properties used in the CSDMS
   wiki?
1. How can one show the data for *all* the properties of a particular
   model?


## Additional references

* Properties: https://www.semantic-mediawiki.org/wiki/Help:Properties_and_types
* Results formats: https://www.semantic-mediawiki.org/wiki/Help:Result_formats
* Categories: https://meta.wikimedia.org/wiki/Help:Category
