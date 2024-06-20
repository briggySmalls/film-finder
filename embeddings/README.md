# Embeddings

Pipline for generating embeddings for documents.

## Coercing

Flatten the data into a single object:

```
jq -c "{id: ._id} + ._source" ../filmfinder.vespa.app/ext/tmdb-dump.json > ../filmfinder.vespa.app/ext/tmdb-dump-flattened.jsonl
```

Then add the embeddings

```
poetry run embeddings ../filmfinder.vespa.app/ext/2-examples-flattened.jsonl ../filmfinder.vespa.app/ext/2-examples-flat-w-embeddings.jsonl
```

Then coerce into a format for vespa:

```
jq -c "{put:(\"id:film:film::\" + (.id | tostring)) , fields: {id, title, overview, tagline, release_date, genres, cast, directors}}" tmdb-dump-flat-w-embeddings.jsonl > tmdb-dump-vespa.jsonl
```
