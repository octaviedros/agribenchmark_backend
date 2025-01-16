# update_schema.py
import os
from config import username, password, db

uri = f"host='localhost' dbname='{db}' user='{username}' password='{password}'"

if __name__ == "__main__":
    sql_schema_dir = 'schema'
    command = f"pg-schema-diff apply --dsn 'postgres://{username}:{password}@localhost:5432/{db}' --schema-dir {sql_schema_dir} --allow-hazards DELETES_DATA"
    os.system(command)

