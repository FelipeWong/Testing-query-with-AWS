SELECT articles.title, articles.ID, COUNT(clickstream.objectId) AS like_received 
FROM articles, clickstream 
WHERE articles.ID = clickstream.objectId AND 
(clickstream.time BETWEEN "2017-04-01 00:00:00" AND "2017-04-01 23:59:59") 
GROUP BY articles.title, articles.ID 
ORDER BY like_received DESC 
LIMIT 10;