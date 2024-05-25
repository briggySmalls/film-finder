# Film Finder

## TMDB

The data used in this project was lifted from the movie database.

It was modified using:

```bash
cat tmdb-dump.json | jq -c '{put: ("id:film:film::" + (._id|tostring)), fields: {id: ._id, title:._source.title, overview:._source.overview, tagline:._source.tagline, release_date:._source.release_date, genres: ._source.genres, cast: ._source.cast, directors:._source.directors}}' > tmdb-dump-vespa.jsonl
```
