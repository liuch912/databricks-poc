from databricks import sql
import os

connection = sql.connect(
                        server_hostname = os.getenv("DATABRICKS_HOST"),
                        http_path = os.getenv("DATABRICKS_HTTP_PATH"),
                        access_token = os.getenv("DATABRICKS_TOKEN"))

cursor = connection.cursor()

cursor.execute("SELECT order_item_id, sku_price_usd FROM hive_metastore.dw_data_model.fact_order_item WHERE order_number = 451961021")
results = cursor.fetchall()
for result in results:
    print(result.order_item_id)
# print(cursor.fetchall())

cursor.close()
connection.close()