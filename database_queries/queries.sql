SELECT C.customer_id, C.name, SUM(OD.quantity) AS total_books
FROM Customers C
JOIN Orders O ON C.customer_id = O.customer_id
JOIN OrderDetails OD ON O.order_id = OD.order_id
WHERE O.order_date >= NOW() - INTERVAL 1 YEAR
GROUP BY C.customer_id, C.name
ORDER BY total_books DESC
LIMIT 5;











SELECT B.author, SUM(B.price * OD.quantity) AS total_revenue
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.author
ORDER BY total_revenue DESC;











SELECT B.title, SUM(OD.quantity) AS total_quantity
FROM Books B
JOIN OrderDetails OD ON B.book_id = OD.book_id
GROUP BY B.title
HAVING total_quantity > 10;
