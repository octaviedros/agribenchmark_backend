import uuid
from pathlib import Path

import polars as pl
from fastapi import APIRouter, BackgroundTasks, Response
from fastapi.responses import FileResponse

from src.database import DATABASE_URL, tables_general_id

export_router = APIRouter(prefix="/export", tags=["export"])

def remove_file(temp_file):
    Path(temp_file).unlink()

@export_router.get("/farm/{general_id}")
def export_to_csv(general_id: str, background_tasks: BackgroundTasks, format: str = "csv", ):
  # Collect data from all tables
  data = {
    table: pl.read_database_uri(
      f"SELECT * FROM {table} WHERE general_id = '{general_id}'", DATABASE_URL, engine="connectorx"
    ) for table in tables_general_id
  }
  # Check if any table is empty
  # If empty, create a table with the same schema and add a row with None values
  for tbl in data:
    if data[tbl].height == 0:
      sch = data[tbl].schema
      data[tbl] = pl.DataFrame(
        [{
          col: general_id if col == "general_id" else None
          for col in sch.keys()
        }],
        schema=sch
      )
      
  # add a table column to each table, melt, and vstack
  data = pl.concat(
    [
      data[table]
        .with_row_index("row_index")
        .with_columns(
          pl.lit(table).alias("table")
        )
        .melt(id_vars=["general_id", "table", "row_index"]) for table in tables_general_id
    ], 
    how="vertical"
  )
  if format == "json":
    # write to json
    headers = {'Content-Disposition': 'attachment; filename="data.json"'}
    return Response(data.write_json(), headers=headers, media_type="application/json")
  elif format == "xlsx":
    # write to xlsx
    unique_name = str(uuid.uuid4())
    temp_file= unique_name+".xlsx"
    headers = {'Content-Disposition': 'attachment; filename="data.xlsx"'}
    data.write_excel(temp_file)
    file_response = FileResponse(temp_file,headers=headers, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    background_tasks.add_task(remove_file,temp_file)
    return file_response
  else:
    # write to csv
    headers = {'Content-Disposition': 'attachment; filename="data.csv"'}
    return Response(data.write_csv(), headers=headers, media_type="text/csv")  

  