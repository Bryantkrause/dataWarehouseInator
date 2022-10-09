-- will it update?
UPDATE invoice, invoiceconnector
SET location = 'None'
WHERE invoiceconnector.InvoiceUniqueKey = '239702Lyneer Staffing'
-- yes but I should probably add something called a forieng key

ALTER TABLE invoiceconnector
ADD COLUMN invoice_id BIGINT NOT NULL DEFAULT 0;

UPDATE invoiceconnector
INNER JOIN invoice ON  invoice.InvoiceUniqueKey = invoiceconnector.InvoiceUniqueKey
SET invoiceconnector.invoice_id = invoice.invoice_id;

ALTER TABLE invoiceconnector
ADD FOREIGN KEY (invoice_id) REFERENCES invoice(invoice_id);

-- ALTER TABLE invoiceconnector
-- MODIFY COLUMN invoice_id BIGINT

