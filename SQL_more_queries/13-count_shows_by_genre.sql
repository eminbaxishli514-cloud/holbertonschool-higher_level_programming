-- 13-count_shows_by_genre.sql
SELECT g.name AS genre, COUNT(tg.show_id) AS number_of_shows
FROM tv_genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
GROUP BY g.id
ORDER BY number_of_shows DESC;

