#!/usr/bin/python3
""" Lists all cities from the database """
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC;",
                (sys.argv[4], ))
    states = cur.fetchall()
    sep = ""
    for state in states:
        print("{}{}".format(sep, state[1]), end="")
        sep = ", "
    print()
