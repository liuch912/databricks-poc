# DataBricks POC

## Background
 
This POC intend to figure out how to access the DataBricks' data.

## Steps

### Create or Find the SQL Warehouse

- Set the environment variables

```
export DATABRICKS_HOST=
export DATABRICKS_TOKEN=          # get it from your personal account or service principals
export DATABRICKS_HTTP_PATH=      # from the connection detail of warehouse
export DATABRICKS_CATALOG=
export DATABRICKS_SCHEMA=
# export DATABRICKS_ACCOUNT_ID=

```

### Create DataBricks Query
`databricks_query.sh`

### Use SQLAlchemy to execute SQL
`sqlalchemy_test.py`

### Use databricks-sql-connector
`databricks_sql.py`