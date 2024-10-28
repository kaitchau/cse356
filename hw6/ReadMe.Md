Homework #6
Description

1. Install Elasticsearch with Kibana (elastic version >=6x)
2. Create an index called “hw7”
3. Populate the index with IMDB data about some relatively recent movies
(https://grading.cse356.compas.cs.stonybrook.edu/hw7/movies.json)
(hint, use a script or logstash)
4. Create a visualization titled with your submission id to chart the top rated movie for every year and the average movie earnings for each year.
(note: don’t forget to open the appropriate default port(s) for both Elasticsearch and
Kibana in the security group settings, as we will be accessing Elasticsearch and Kibana
via your-website.com:port)

-----------------------------------------------------------------------

- Install Docker

https://docs.docker.com/engine/install/ubuntu/


- Install Elasticsearch / kibana version 8.15 w/ docker

https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html


- $ docker run --name es01 --net elastic -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.15.3

- $ docker run --name kib01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.15.3s

- Open new ubunti linux wsl terminal to use, since the elasticsearch is running on the other tab of wsl. Create the index with cmd $ curl -X PUT "localhost:9200/hw7?pretty"
- Download the movies json to the cloud linux server w/ cmd $ wget -O ./movies.json https://grading.cse356.compas.cs.stonybrook.edu/hw7/movies.json , where ./movies.json is the file path u want.
- Ensure logstash is installed w/ cmd $ sudo apt-get install logstash
- $ /usr/share/logstash/bin/logstash -f ./movies.conf
- Start Kibana w/ $ sudo systemctl start kibana

- $ curl -X PUT "http://localhost:9200/cse356"

- $ sudo apt update
- $ sudo apt install python3
- $ sudo apt install pip
- $ sudo apt install python3-pip
- $ pip install elasticsearch
<br/> run the movies.py script w/ $ python3 movies.py

## Configure Kabana to the below address.
- http://130.245.136.153:9200

### to make sure that the script properly indexed the json
- $ curl -X GET "http://localhost:9200/cse356/_search?pretty"