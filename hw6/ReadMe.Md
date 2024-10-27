- Update pkg manager + install Java

$ sudo apt-get update
$ sudo apt-get install openjdk-11-jdk -y
$ update-alternatives --config java
$ echo "JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64" | sudo tee -a /etc/environment
source /etc/environment

- Install Elasticsearch (for Ubuntu)
$ wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo apt-get install apt-transport-https
$  echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
$ sudo apt-get update && sudo apt-get install elasticsearch