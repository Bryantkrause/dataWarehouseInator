WITH CTE(InvoiceNumber, 
    vendor, coolid,
    duplicatecount)
AS (SELECT InvoiceNumber, 
           vendor, coolid,
           ROW_NUMBER() OVER(PARTITION BY InvoiceNumber, 
                                          vendor
           ORDER BY coolid) AS DuplicateCount
    FROM rawdata)
SELECT *
FROM CTE;
-- learn to merge https://www.sqlshack.com/understanding-the-sql-merge-statement/


CREATE PROCEDURE dbo.atp_schema_mapping
       @schema_name SYSNAME,
       @table_name SYSNAME,
       @where_clause VARCHAR(MAX) = ''
AS
BEGIN
       SET NOCOUNT ON;
 
       DECLARE @sql_command VARCHAR(MAX) = ''; -- Used for many dynamic SQL statements
     
       SET @where_clause = ISNULL(LTRIM(RTRIM(@where_clause)), ''); -- Clean up WHERE clause, to simplify future SQL
       DECLARE @row_counts TABLE -- Temporary table to dump dynamic SQL output into
              (row_count INT);
 
       DECLARE @base_table_row_count INT; -- This will hold the row count of the base entity.
       SELECT @sql_command = 'SELECT COUNT(*) FROM [' + @schema_name + '].[' + @table_name + ']' + -- Build COUNT statement
              CASE
                     WHEN @where_clause <> '' -- Add WHERE clause, if provided
                           THEN CHAR(10) + 'WHERE ' + @where_clause
                     ELSE ''
              END;
 
       INSERT INTO @row_counts
              (row_count)
       EXEC (@sql_command);
      
       SELECT
              @base_table_row_count = row_count -- Extract count from temporary location.
       FROM @row_counts;
 
       -- If there are no matching rows to the input provided, exit immediately with an error message.
       IF @base_table_row_count = 0
       BEGIN
              PRINT '-- There are no rows to process based on the input table and where clause.  Execution aborted.';
              RETURN;
       END
END
GO
-- https://www.sqlshack.com/mapping-schema-and-recursively-managing-data-part-1/








