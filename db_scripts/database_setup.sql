-- File: db_scripts/database_setup.sql

-- 1. Create the table for test users
CREATE TABLE IF NOT EXISTS test_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    should_pass BOOLEAN NOT NULL,
    error_msg TEXT
);

-- 2. Clear existing data (to avoid duplicates if run multiple times)
TRUNCATE TABLE test_users RESTART IDENTITY;

-- 3. Insert the JSON data into the table
INSERT INTO test_users (username, password, should_pass, error_msg) VALUES
    ('standard_user', 'secret_sauce', TRUE, ''),
    ('locked_out_user', 'secret_sauce', FALSE, 'Epic sadface: Sorry, this user has been locked out.'),
    ('invalid_user', 'wrong_password', FALSE, 'Epic sadface: Username and password do not match any user in this service');

-- 4. Verify data (Select it to check)
SELECT * FROM test_users;