import sqlite3


class SqliteUtils:
    def __init__(self):
        pass

    @staticmethod
    def create_connection(db_path):
        if db_path:
            return sqlite3.connect(db_path)

    @staticmethod
    def create_cursor(connection):
        if connection:
            return connection.cursor()


if __name__ == "__main__":
    main = SqliteUtils()


