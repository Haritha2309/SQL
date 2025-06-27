import pyodbc
class Connection:
    def get_connection(self):
        self.server = r'LAPTOP-VLGRVLCM'         
        self.database = 'hospital'     

        self.conn_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            "Trusted_Connection=yes;"
        )
        self.conn = pyodbc.connect(self.conn_str)
        print("successful")
        return self.conn

con = Connection()
con.get_connection()