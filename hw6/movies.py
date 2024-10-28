from elasticsearch import Elasticsearch
import json

# Create an instance of the Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme':'http'}])

# Index name
index_name = "cse356"

# Create the index if it doesn't exist
es.indices.create(index=index_name)

# Load the movie data from the JSON file
with open('movies.json') as f:
    movies = json.load(f)

# Index each movie in the Elasticsearch index
for movie in movies:
    es.index(index=index_name, body=movie)

print("Movies indexed successfully!")