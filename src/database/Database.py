import pandas as pd
import mysql.connector

class Database:
    def __init__(self, host, port, user, password, database=None):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor(buffered=True)

    def createTable(self, table_name, columns):
        columns_definition = ", ".join([f"{name} {datatype}" for name, datatype in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definition})")

    def insertData(self, table_name, row_data):
        placeholders = ", ".join(["%s"] * len(row_data))
        columns = ", ".join(row_data.keys())
        values = tuple(row_data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()
        

    def updateData(self, table_name, updates, condition):
        """Update data in a table"""
        set_clause = ", ".join([f"{col} = %s" for col in updates.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, tuple(updates.values()))
        self.connection.commit()

    def selectData(self, query, row=None, flag="all"):
        self.cursor.execute(query, row)
        if flag == "one":
            results = self.cursor.fetchone()
        else:
            results = self.cursor.fetchall()
        return results

    def closeConnection(self):
        self.cursor.close()
        self.connection.close()