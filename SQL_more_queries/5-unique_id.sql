#!/usr/bin/sql
-- Create table unique_id with id DEFAULT 1 and UNIQUE constraint

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
