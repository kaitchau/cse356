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