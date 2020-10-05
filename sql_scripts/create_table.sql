CREATE TABLE todoapp.todo
(
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    description text,
    status character varying(32) NOT NULL DEFAULT 'New',
    PRIMARY KEY (id)
);

ALTER TABLE todoapp.todo
    OWNER to todoapp;