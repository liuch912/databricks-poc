import os
from sqlalchemy import create_engine
from sqlalchemy import text

access_token    = os.getenv("DATABRICKS_TOKEN")
server_hostname = os.getenv("DATABRICKS_HOST")
http_path       = os.getenv("DATABRICKS_HTTP_PATH")
catalog         = os.getenv("DATABRICKS_CATALOG")
schema          = os.getenv("DATABRICKS_SCHEMA")

engine = create_engine(
  url = f"databricks://token:{access_token}@{server_hostname}?" +
        f"http_path={http_path}&catalog={catalog}&schema={schema}"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT order_item_id FROM hive_metastore.dw_data_model.fact_order_item WHERE order_number = 451961021"))
    print(result)
    for row in result:
        print("order_item_id:", row.order_item_id)

