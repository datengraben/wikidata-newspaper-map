#!/bin/env sh
QUERY=`cat $1`
curl -G https://query.wikidata.org/sparql \
	--header "Accept: text/csv"  \
	--data-urlencode query="${QUERY}"
