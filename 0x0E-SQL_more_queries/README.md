QL - More queries

This project acquinted me with the knowledge of the following;

i) How to create a new MySQL user
ii) How to manage privileges for a user to a database or table
iii) What’s a PRIMARY KEY
iv) What’s a FOREIGN KEY
v) How to use NOT NULL and UNIQUE constraints
vi) How to retrieve datas from multiple tables in one request
vii) What are subqueries
viii) What are JOIN and UNION

The following are the files use to execute the corresponding fuctions;

0-privileges.sql - Writes a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on my server (in localhost).

1-create_user.sql - Writes a script that creates the MySQL server user user_0d_1.

2-create_read_user.sql - Writes a script that creates the database hbtn_0d_2 and the user user_0d_2.

3-force_name.sql - Writes a script that creates the table force_name on your MySQL server.

4-never_empty.sql - Writes a script that creates the table id_not_null on your MySQL server.

5-unique_id.sql - Writes a script that creates the table unique_id on your MySQL server.

6-states.sql - Writes a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

7-cities.sql - Writes a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

8-cities_of_california_subquery.sql - Writes a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

9-cities_by_state_join.sql - Writes a script that lists all cities contained in the database hbtn_0d_usa.

10-genre_id_by_show.sql - Writes a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

11-genre_id_all_shows.sql - Writes a script that lists all shows contained in the database hbtn_0d_tvshows.

12-no_genre.sql - Writes a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

13-count_shows_by_genre.sql - Writes a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

14-my_genres.sql - Writes a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

15-comedy_only.sql - Writes a script that lists all Comedy shows in the database hbtn_0d_tvshows.

16-shows_by_genre.sql - Writes a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

100-not_my_genres.sql - Writes a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.

101-not_a_comedy.sql - Writes a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

102-rating_shows.sql - Writes a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

103-rating_genres.sql - Writes a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
