from config.database import Database
from src.utils.init_tables import InitializeTables

if __name__ == '__main__':
    db = Database()
    tables = InitializeTables(database=db)
    tables.drop_tables()
