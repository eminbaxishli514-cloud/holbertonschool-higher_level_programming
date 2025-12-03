-- 13-count_shows_by_genre.sql
-- Count the number of shows linked to each genre using only tv_show_genres

SELECT genre_id AS genre, COUNT(show_id) AS number_of_shows
FROM tv_show_genres
GROUP BY genre_id
ORDER BY number_of_shows DESC;
