-- 16-shows_by_genre.sql
SELECT t.title, g.name
FROM tv_shows t
LEFT JOIN tv_show_genres tg ON t.id = tg.show_id
LEFT JOIN tv_genres g ON tg.genre_id = g.id
ORDER BY t.title ASC, g.name ASC;
