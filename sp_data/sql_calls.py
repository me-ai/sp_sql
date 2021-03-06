# SQL Scripts
query_mdm_inventory = (
"""SELECT
[InventoryItemID]
,[ProductIdentifier]
,[Name]
,[Description]
,[AssetIdentifier]
,[MinOrderQuantity]
,[AverageCost]
,[LastCost]
,[LastSalePrice]
,[StockType]
,[ChangeDate]
,[ChangeUser]
,[IsDeleted]
,[CreateUser]
,[CreateDate]
,[Archived]
,[SiteCodeID]
,[IsCoreItem]
,[CoreValue]
,[RequiresUniqueClaim]
,[AllowNewStoreroomOnReceipt]
,[ServiceTypeID]
,[IsReadOnlyRecord]
,[PhysicalCountCycleCountDays]
,[IndirectProcurementMaxPrice]
FROM [sysco_reporting].[dbo].[InventoryItem]
WHERE [SiteCodeID] LIKE '%-1%' and [Archived] = 0"""
)
