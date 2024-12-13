# Von CoPilot eine erstellt für die create_update_tables.py als verbesserter Code vorgschlagen:
#   import subprocess
# from config import username, password, db

# if __name__ == "__main__":
#     sql_schema_dir = 'schema'
#     command = f"pg-schema-diff apply --dsn 'postgres://{username}:{password}@localhost:5432/{db}' --schema-dir {sql_schema_dir}"
    
#     try:
#         result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         print(f"Output: {e.output}")        