CREATE DATABASE todoapp
    WITH 
    OWNER = todoapp
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE todoapp TO todoapp;