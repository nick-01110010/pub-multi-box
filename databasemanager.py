import mysql.connector
import configparser 
 
class DatabaseManager:
    def __init__(self, config_file="config.ini", default="enb_multi_box"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        self.host = self.config.get("Database", "host")
        self.user = self.config.get("Database", "user")
        self.password = self.config.get("Database", "password")
        self.default = default
        self.connection = None
        self.cursor = None
        self.database = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        self.database = self.default

        self.cursor.execute("SHOW DATABASES LIKE %s", (self.database,))
        if not self.cursor.fetchone():
            self.cursor.execute(f"CREATE DATABASE {self.database}")
            self.connection.commit()

        self.connection.database = self.database
        self._create_tables()

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

    def _create_tables(self):
        create_characters_table_query = """
        CREATE TABLE IF NOT EXISTS characters (
            character_id INT AUTO_INCREMENT PRIMARY KEY,
            character_name VARCHAR(20) NOT NULL,
            character_password VARCHAR(20) NOT NULL,
            character_level INT NOT NULL
            character_class VARCHAR(2) NOT NULL,
            character_weaopon_slots INT NOT NULL
            character_device_slots INT NOT NULL
            character_fleet_position INT NOT NULL
        )
        """
        self.cursor.execute(create_characters_table_query)
        self.connection.commit()