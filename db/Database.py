import sqlite3


class DB(object):
    """DB initializes and manipulates SQLite3 databases."""

    def __init__(self, database='database.db', statements=None):
        """Initialize a new or connect to an existing database.

        Accept setup statements to be executed.
        """

        # the database filename
        self.database = database
        # holds incomplete statements
        self.statement = ''
        # indicates if selected data is to be returned or printed
        self.display = False
        if statements is None:
            statements = []

        self.connect()

        # execute setup satements
        self.execute(statements)

        self.close()

    def connect(self):
        """Connect to the SQLite3 database."""

        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()
        self.connected = True
        self.statement = ''

    def close(self):
        """Close the SQLite3 database."""

        self.connection.commit()
        self.connection.close()
        self.connected = False

    def incomplete(self, statement):
        """Concatenate clauses until a complete statement is made."""

        self.statement += statement
        if self.statement.count(';') > 1:
            print('An error has occurerd: ' +
                  'You may only execute one statement at a time.')
            print('For the statement: {self.statement}')
            self.statement = ''
        if sqlite3.complete_statement(self.statement):
            # the statement is not incomplete, it's complete
            return False
        else:
            # the statement is incomplete
            return True

    def execute(self, statements):
        """Execute complete SQL statements.

        Incomplete statements are concatenated to self.statement until they 
        are complete.

        Selected data is returned as a list of query results. Example: 

        for result in db.execute(queries):
            for row in result:
                print row
        """

        queries = []
        close = False
        if not self.connected:
            # open a previously closed connection
            self.connect()
            # mark the connection to be closed once complete
            close = True
        if type(statements) == str:
            # all statements must be in a list
            statements = [statements]
        for statement in statements:
            if self.incomplete(statement):
                # the statement is incomplete
                continue
            # the statement is complete
            try:
                statement = self.statement.strip()
                # reset the test statement
                self.statement = ''
                self.cursor.execute(statement)
                # retrieve selected data
                data = self.cursor.fetchall()
                if statement.upper().startswith('SELECT'):
                    # append query results
                    queries.append(data)

            except sqlite3.Error as error:
                print('An error occurred:', error.args[0])
                print('For the statement:', statement)

        # only close the connection if opened in this function
        if close:
            self.close()
        # print results for all queries
        if self.display:
            for result in queries:
                if result:
                    for row in result:
                        print(row)
                else:
                    print(result)
        # return results for all queries
        else:
            return queries
