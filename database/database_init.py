import mysql.connector


def init_tables(host="localhost", user="root", password="maslo", database="korpo"):
    with mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
    ) as connection:
        with connection.cursor() as cursor:

            cursor.execute("""
             CREATE TABLE IF NOT EXISTS employees (
                    id INT PRIMARY KEY,
                    name VARCHAR(50) COLLATE utf8mb4_unicode_ci,
                    surname VARCHAR(50) COLLATE utf8mb4_unicode_ci,
                    salary INT,
                    energy INT
                )
            """)
            print("Tabela 'employees' utworzona.")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS managers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    employee_id INT,
                    team_size INT
                )
            """)
            print("Tabela 'managers' utworzona.")

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS workers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    employee_id INT,
                    quota INT,
                    manager_id INT
                )
            """)
            print("Tabela 'workers' utworzona.")
