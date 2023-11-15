UPDATE products
SET product_price = REPLACE(product_price, '£', '')
WHERE product_price LIKE '£%';