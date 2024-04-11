from abc import ABC, abstractmethod


# Abstract base class for database connections
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass


# Concrete implementations for different database systems
class OracleConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to Oracle database...")


class MySQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to MySQL database...")


class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to PostgreSQL database...")


# Abstract factory class for creating database connections
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass


# Concrete factory implementations for different database systems
class OracleConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return OracleConnection()


class MySQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()


class PostgreSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()


# Client class to use database connections
class DatabaseClient:
    def __init__(self, connection_factory: DatabaseConnectionFactory):
        self.connection_factory = connection_factory

    def connect_to_database(self):
        connection = self.connection_factory.create_connection()
        connection.connect()
