Homework #5
Description

1. Install nginx.

2. Configure it as a round-robin reverse proxy between these backends:  
- http://grading.cse356.compas.cs.stonybrook.edu:9000
- http://grading.cse356.compas.cs.stonybrook.edu:9001 
- http://grading.cse356.compas.cs.stonybrook.edu:9002

3. Make sure failures of a backend server (e.g., timeouts or 50x responses) are not fatal and allow the other backends to handle requests. 

-------------------------------------------

Grading completed. Score: 2

Starting basic round robin test...
Passed basic round robin test = 0.5pts. Now waiting...
Starting test with one server unavailable...
Successfully tested with one server unreachable = 0.5pts. Now waiting...
Starting test with one server failing with Internal Server Error...
Successfully tested with one server having Internal Server Error = 0.5pts. Now waiting...
Starting round robin test after server recovery...
Passed round robin test after server recovery = 0.5pts. All tests passed!

-------------------------------------------
First, install NGINX:
sudo apt update
sudo apt install nginx

Create/edit the NGINX configuration file (thats the file above):
sudo nano /etc/nginx/conf.d/upstream.conf

Remove the default NGINX configuration (not optional):
sudo rm /etc/nginx/sites-enabled/default

Test the configuration:
sudo nginx -t

If the test is successful, restart NGINX:
sudo systemctl restart nginx

To verify it's working:
curl http://localhost/