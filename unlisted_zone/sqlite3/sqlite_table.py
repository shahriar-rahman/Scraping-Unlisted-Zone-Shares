import sqlite3


class Connection:
    def __init__(self):
        self.connection = sqlite3.connect('../../database/db_unlisted.db')

    def create_table(self):
        cursor = self.connection.cursor()

        cursor.execute('''create table if not exists unlisted_shares(
        company text,
        lot_size text,
        last_price text,
        cost_per_lot text)
        ''')
        self.connection.commit()

    def inspect_table(self):
        cursor = self.connection.cursor()
        data = cursor.execute('''select * from 
        unlisted_shares''')

        for row in data:
            print(row)

    def close_db(self):
        self.connection.close()


if __name__ == "__main__":
    main = Connection()
    main.create_table()
    main.inspect_table()
    main.close_db()
