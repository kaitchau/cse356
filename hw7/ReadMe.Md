Homework #7
Description

1. Install a mysql variant. (mysql, maria, percona, ...)
2. Create a database called 'hw9'.
3. Create a table called "assists" and import MLS 2017 data for assists by soccer players. (https://github.com/jokecamp/FootballData/blob/master/MLS/2017/assists.csv)
4. Create a REST service to access the data and return results of the following query for a given player at A.Player='PLAYER_NAME_HERE':
select A.Player as p1,B.Player as p2,C.Player as p3,D.Player as p4 from assists A, assists B, assists C, assists D where A.POS=B.POS and B.POS=C.POS and C.POS=D.POS and A.Club<>B.Club and A.club<>C.Club and A.Club<>C.Club and A.Club<>D.Club and B.Club<>C.Club and B.Club<>D.Club and C.Club<>D.Club and A.Player='PLAYER_NAME_HERE' order by A.A+B.A+C.A+D.A desc, A.A desc, B.A desc, C.A desc, D.A desc, p1, p2, p3, p4 limit 1;
Add a X-CSE356 header with your submission ID as the value to all your responses.
GET /hw9?player=PLAYER_NAME_HERE should respond with:
    {
       players: String[]
    }
Note: players is the array of all names returned by the query.
5. Install memcached.
6. Integrate memcached caching to speed up the REST-based service.

------------------------

