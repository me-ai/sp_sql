import pyodbc
from sp_data.secrets import secret_user, secret_password, server_ip, reporting_database
from sp_data.sql_calls import query_mdm_inventory
import pandas as pd

server = server_ip
database = reporting_database
username = secret_user
password = secret_password
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
query = query_mdm_inventory

## Specify comuns for csv
col_names = [
    'InventoryItemID',
    'ProductIdentifier',
    'Name',
    'Description',
    'AssetIdentifier',
    'MinOrderQuantity',
    'AverageCost',
    'LastCost',
    'LastSalePrice',
    'StockType',
    'ChangeDate',
    'ChangeUser',
    'IsDeleted',
    'CreateUser',
    'CreateDate',
    'Archived',
    'SiteCodeID',
    'IsCoreItem',
    'CoreValue',
    'RequiresUniqueClaim',
    'AllowNewStoreroomOnReceipt',
    'ServiceTypeID',
    'IsReadOnlyRecord',
    'PhysicalCountCycleCountDays',
    'IndirectProcurementMaxPrice'
]

SQL_Query = pd.read_sql_query(query, cnxn)
pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(SQL_Query, columns=col_names)
print(df)
df.to_csv('test.csv')
print('CSV complete!')
