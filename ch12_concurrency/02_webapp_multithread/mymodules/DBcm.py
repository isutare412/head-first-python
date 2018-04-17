import mysql.connector


class DBError(Exception):
    pass


class UseDatabase:
    def __init__(self, **config: dict) -> None:
        self.config = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.Error as err:
            raise DBError(err)

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is not None:
            raise DBError(exc_value)
