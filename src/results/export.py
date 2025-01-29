from fastapi import Response, APIRouter
import polars as pl
from src.database import tables_general_id, DATABASE_URL

export_router = APIRouter(prefix="/export", tags=["export"])

@export_router.get("/farm/{general_id}")
def export_to_csv(general_id: str, format: str = "csv"):
  # Collect data from all tables
  data = {
    table: pl.read_database_uri(
      f"SELECT * FROM {table} WHERE general_id = '{general_id}'", DATABASE_URL, engine="connectorx"
    ) for table in tables_general_id
  }
  # add a table column to each table, melt, and vstack
  data = pl.concat(
    [
      data[table]
        .with_columns(
          pl.lit(table).alias("table")
        )
        .melt(id_vars=["general_id", "table"]) for table in tables_general_id
    ], 
    how="vertical"
  )
  if format == "json":
    # write to json
    headers = {'Content-Disposition': 'attachment; filename="data.json"'}
    return Response(data.write_json(), headers=headers, media_type="application/json")
  elif format == "xlsx":
    # write to xlsx
    headers = {'Content-Disposition': 'attachment; filename="data.xlsx"'}
    return Response(data.write_excel(), headers=headers, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
  else:
    # write to csv
    headers = {'Content-Disposition': 'attachment; filename="data.csv"'}
    return Response(data.write_csv(), headers=headers, media_type="text/csv")  

  