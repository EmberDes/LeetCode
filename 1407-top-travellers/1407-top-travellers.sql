-- select u.name,ifnull(sum(r.distance),0) as travelled_distance
-- from users  u
-- left join rides  r
-- on u.id=r.user_id
-- group by u.id
-- order by travelled_distance desc,name; 
SELECT name AS name, IFNULL(SUM(distance),0) AS travelled_distance 
FROM Users u LEFT JOIN Rides r 
ON u.id = r.user_id 
GROUP BY u.id 
ORDER BY travelled_distance DESC, u.name ASC; 
