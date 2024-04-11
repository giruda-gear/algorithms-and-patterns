import pytest
from solutions.factory_db_connection import (
    OracleConnectionFactory,
    MySQLConnectionFactory,
    PostgreSQLConnectionFactory,
    DatabaseClient,
)


@pytest.fixture
def oracle_factory():
    return OracleConnectionFactory()


@pytest.fixture
def mysql_factory():
    return MySQLConnectionFactory()


@pytest.fixture
def postgresql_factory():
    return PostgreSQLConnectionFactory()


def test_oracle_connection(oracle_factory, capsys):
    client = DatabaseClient(oracle_factory)
    client.connect_to_database()
    captured = capsys.readouterr()
    assert "Connecting to Oracle database..." in captured.out


def test_mysql_connection(mysql_factory, capsys):
    client = DatabaseClient(mysql_factory)
    client.connect_to_database()
    captured = capsys.readouterr()
    assert "Connecting to MySQL database..." in captured.out


def test_postgresql_connection(postgresql_factory, capsys):
    client = DatabaseClient(postgresql_factory)
    client.connect_to_database()
    captured = capsys.readouterr()
    assert "Connecting to PostgreSQL database..." in captured.out
