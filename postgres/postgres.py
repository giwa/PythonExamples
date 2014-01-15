#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2
'''
try:
    con = psycopg2.connect("dbname='campus' user='postgres' host='localhost' password='postgres'")
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = con.cursor()
    # execute our Query
    cursor.execute("INSERT INTO updatemeta(key, value) VALUES('Foo', 'Bar')")
    con.commit()

    cur = con.cursor()
    cur.execute("SELECT * FROM updatemeta")
    rows = cur.fetchall()

    for row in rows:
        print row

except psycopg2.DatabaseError as e:
    if con:
        con.rollback()
    print e

finally:
    if con:
        con.close()
'''

class BasePostgres:
    def __init__(self, database='campus', user='postgres', host='localhost', password='postgres'):
        self._con = psycopg2.connect(database=database, user=user, host=host, password=password)

    def __enter__(self):
        return self

    def __exit__(self):
        self._con.close()

    def __del__(self):
        self._con.close()

class PostgresContextMnager(BasePostgres):
    def __init__(self):
        super(PostgresContextMnager,self).__init__()

    def __enter__(self):
        super(PostgresContextMnager,self).__enter__()

    def __exit__(self):
        super(PostgresContextMnager,self).__exit__()

    def Insert(self, sql):
        self.cursor = self._con.cursor()
        self.cursor.execute(sql)
        self._con.commit()

    def Select(self, sql):
        self.cursor = self._con.cursor()
        self.cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            yield row 
            return

    def Update(self, sql):
        self.cursor = self._con.cursor()
        self.cursor.execute("SQL")
        self._con.commit()

class PostgresDict(BasePostgres):
    def __init__(self):
        super(PostgresContextMnager,self).__init__()

    def __setitem__(self, key, value):
        try:
            self.cursor = self._con.cursor()
            sql = "UPDATE updatemeta SET value='{0}' WHERE key='{1}'".format(key, value)
            self.cursor.execute(sql)
            sql = '''INSERT INTO updatemeta (key, value)
                        SELECT '{0}', '{1}'
                        WHERE NOT EXISTS (SELECT 1 FROM updatemeta WHERE key = '{0}')
            '''.format(key,value)
            self.cursor.execute(sql)
            self._con.commit()
        except psycopg2.ProgrammingError as e:
            print e
            return None
            self._con.rollback()

    def __getitem__(self, key):
        try:
            self.cursor = self._con.cursor()
            sql = "SELECT value FROM updatemeta WHERE key = '{0}'".format(key)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except psycopg2.ProgrammingError as e:
            print e
            return None
        if rows:
            return rows[0][0]
        else:
            return rows

    def __delitem__(self, key):
        try:
            self.cursor = self._con.cursor()
            sql = "DELETE FROM updatemeta WHERE key = '{0}'".format(key)
            self.cursor.execute(sql)
            self._con.commit()
        except:
            self._con.rollback()
            return False
        return True

    def _getKeys(self):
        try:
            self.cursor = self._con.cursor()
            sql = "SELECT key FROM updatemeta"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except psycopg2.ProgrammingError as e:
            return False
        return rows

    def keys(self):
        for row in self._getKeys():
            yield row[0]

    def _getValues(self):
        try:
            self.cursor = self._con.cursor()
            sql = "SELECT value FROM updatemeta"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except psycopg2.ProgrammingError as e:
            return False
        return rows

    def values(self):
        for row in self._getValues():
            yield row[0]

    def _getItems(self):
        try:
            self.cursor = self._con.cursor()
            sql = "SELECT key, value FROM updatemeta"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
        except:
            return False
        return rows

    def items(self):
        for key, value in self._getItems():
            yield (key, value)

if __name__ == '__main__':
    ps = PostgresDict()
    ps['sese'] = 'aaaaa'
    print ps['sese']
    print ps.keys()
    print list(ps.keys())
    for val in ps.values():
        print val
    
    for item in ps.items():
        print item
    


