-- 14-my_genres.sql
SELECT g.name
FROM genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
JOIN tv_shows t ON tg.show_id = t.id
WHERE t.title = 'Dexter'
ORDER BY g.name ASC;
