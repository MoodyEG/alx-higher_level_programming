-- A script that displays the max temperature
-- of each state (ordered by State name).
SELECT state, MAX(value) as max_temp
FROM temperatures
WHERE state IS NOT NULL
GROUP BY state
ORDER BY max_temp DESC;
