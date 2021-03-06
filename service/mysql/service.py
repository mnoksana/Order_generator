from config.constant.exit_code import MYSQL
from config.constant.module import MySQLModule
from util.reporter.reporter import Reporter
import mysql.connector
import logging

LOGGER = logging.getLogger(MySQLModule.SERVICE)


class MySQLService:
    def __init__(self, attempts=15, delay=1):
        self._connection = mysql.connector.MySQLConnection()
        self._attempts = attempts
        self._delay = delay

    def _open(self, host, port, user, password, database, **kwargs):
        self._connection = mysql.connector.connect(**kwargs, host=host, port=port,
                                                   user=user, password=password, database=database)

    def open(self, user, password, database, host="localhost", port=3306, **kwargs):
        try:
            LOGGER.info("Attempting to open connection with MySQL...")
            if kwargs:
                LOGGER.info(f"Connection pool definition with size {kwargs['pool_size']}")
            self._open(host, port, user, password, database, **kwargs)
            LOGGER.info("Connection established successfully")
        except (mysql.connector.DatabaseError, mysql.connector.InterfaceError) as ex:
            LOGGER.fatal(ex)
            exit(MYSQL)

    def _close(self):
        self._connection.close()

    def close(self):
        if self._is_connected():
            self._close()
        LOGGER.info("Connection closed")

    def _reconnect(self):
        try:
            if not self._is_connected():
                LOGGER.info(f"Reconnect to MySQL out of {self._attempts} attempts and delay {self._delay}...")
                self._connection.reconnect(self._attempts, self._delay)
            LOGGER.info("Connection established successfully")
        except mysql.connector.InterfaceError as ex:
            LOGGER.error(ex)
            exit(MYSQL)

    def _execute(self, operation, params, multi):
        cursor = self._connection.cursor()
        cursor.execute(operation, params, multi)
        self._connection.commit()
        return cursor

    def _is_connected(self):
        if self._connection.is_connected():
            return True
        else:
            LOGGER.warning("Connection to MySQL not established")
            return False

    def execute(self, operation, params=(), multi=False):
        try:
            LOGGER.debug(f"Execute with {operation} operation, {params} params and {multi} multi")
            return self._execute(operation, params, multi)
        except mysql.connector.ProgrammingError as ex:
            LOGGER.error(ex)
            self._reconnect()
            return self._execute(operation, params, multi)

    @Reporter.update_time
    @Reporter.update_insertion
    def _execute_many(self, operation, seq_params):
        cursor = self._connection.cursor()
        cursor.executemany(operation, seq_params)
        self._connection.commit()
        return len(seq_params)

    def execute_many(self, operation, seq_params):
        try:
            LOGGER.debug(f"Execute many with {operation} operation")
            return self._execute_many(operation, seq_params)
        except mysql.connector.OperationalError as ex:
            LOGGER.error(ex)
            self._reconnect()
            return self._execute_many(operation, seq_params)

