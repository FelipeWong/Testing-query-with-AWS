SELECT COUNT(DISTINCT articles.userId) 
FROM articles, clickstream 
WHERE articles.ID = clickstream.objectId AND 
(clickstream.time BETWEEN ("2017-04-01 00:00:00" AND "2017-04-01 23:59:59") AND 
clickstream.action = "FIRST_INSTALL") AND 
clickstream.time BETWEEN "2017-04-02 00:00:00" AND "2017-04-08 23:59:59";