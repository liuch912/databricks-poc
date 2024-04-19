from databricks.sdk import WorkspaceClient
import time

w = WorkspaceClient()

srcs = w.data_sources.list()
for src in srcs:
    print(f"{src.id}\t{src.name}")


query = w.queries.create(name=f'sdk-{time.time_ns()}',
                         data_source_id=srcs[0].id,
                         description="test query from Python SDK",
                         query="SELECT order_item_id, sku_price_usd FROM hive_metastore.dw_data_model.fact_order_item WHERE order_number = 451961021")

by_id = w.queries.get(query_id=query.id)

print(by_id)

# cleanup
w.queries.delete(query_id=query.id)
