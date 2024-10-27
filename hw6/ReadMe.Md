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

- Update pkg manager + install Java

## $ sudo apt-get update
## $ sudo apt-get install openjdk-11-jdk -y
## $ update-alternatives --config java
### $ echo "JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" | sudo tee -a /etc/environment
source /etc/environment

- Install Elasticsearch (for Ubuntu)
https://www.elastic.co/guide/en/elasticsearch/reference/6.8/deb.html

$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$  echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install 


- Install Kibana (after Elasticsearch)
https://www.elastic.co/guide/en/kibana/6.8/deb.html


$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$ echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install kibana


- Start Elasticsearch with $ sudo systemctl start elasticsearch
- Open new ubunti linux wsl terminal to use, since the elasticsearch is running on the other tab of wsl. Create the index with cmd $ curl -X PUT "localhost:9200/hw7?pretty"
