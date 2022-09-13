
Setting environment for using XAMPP for Windows.
hp@DESKTOP-H7IKDUM c:\xampp
# mysql -u root
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 12
Server version: 10.4.24-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use gym
Database changed
MariaDB [gym]> show tables;
+---------------+
| Tables_in_gym |
+---------------+
| aa            |
| bb            |
+---------------+
2 rows in set (0.001 sec)

MariaDB [gym]> select * from aa;
+----------+----------+
| username | password |
+----------+----------+
| pasha    | pasha07  |
+----------+----------+
1 row in set (0.000 sec)

MariaDB [gym]> select * from bb;
+-------+----------+------------+----------------+-------------------+------+------------+
| gymid | name     | your_plain | contact_number | aadharcard_number | age  | membership |
+-------+----------+------------+----------------+-------------------+------+------------+
|     1 | prashant | 3 months   | 7021911625     | 456865631171      |   22 | Yes        |
+-------+----------+------------+----------------+-------------------+------+------------+
1 row in set (0.000 sec)

MariaDB [gym]>



