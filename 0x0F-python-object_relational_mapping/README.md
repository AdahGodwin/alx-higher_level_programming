Python - Object-relational mapping

This Project focus on the following;
Python
OOP
SQL
MySQL
ORM
SQLAlchemy

LEARNING OBJECTIVES
At the end of this project, I got acquinted with the following;
Why Python programming is awesome.
How to connect to a MySQL database from a Python script.
How to SELECT rows in a MySQL table from a Python script.
How to INSERT rows in a MySQL table from a Python script.
What ORM means.
How to map a Python Class to a MySQL table.

The files below were created to output the following functions;

0-select_states.py - Writes a script that lists all states from the database hbtn_0e_0_usa:

1-filter_states.py - Writes a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

2-my_filter_states.py - Writes script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

3-my_safe_filter_states.py - Writes a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!.

4-cities_by_state.py - Writes a script that lists all cities from the database hbtn_0e_4_usa.

5-filter_cities.py - Writes a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa.

model_state.py - Writes a python file that contains the class definition of a State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and can’t be null

7-model_state_fetch_all.py - Writes a script that lists all State objects from the database hbtn_0e_6_usa.

8-model_state_fetch_first.py - Writes a script that prints the first State object from the database hbtn_0e_6_usa.

9-model_state_filter_a.py - Writes a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.

10-model_state_my_get.py - Writes a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.

11-model_state_insert.py - Writes a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa.

12-model_state_update_id_2.py - Writes a script that changes the name of a State object from the database hbtn_0e_6_usa.

13-model_state_delete_a.py Writes - Writes a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.

model_city.py, 14-model_city_fetch_by_state.py - Writes a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

relationship_city.py, relationship_state.py, 100-relationship_states_cities.py - Writes a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa: (100-relationship_states_cities.py).

101-relationship_states_cities_list.py - Writes a script that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa.

102-relationship_cities_states_list.py - Writes a script that lists all City objects from the database hbtn_0e_101_usa.
