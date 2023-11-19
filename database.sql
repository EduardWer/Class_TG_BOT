
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    privileg TEXT NOT NULL,
    user_id INTEGER,
    my_groum text,
    Content_id INTEGER ,
    foreign key (Content_id) references Content(Content_id)
    );



CREATE TABLE IF NOT EXISTS Content(
    Content_id INTEGER PRIMARY KEY,
    Group_id    text,
    Foto_id INTEGER,
    caption  TEXT,
    Content_text TEXT,
    Video_id INTEGER,
    Audio_id INTEGER
);
DROP table Users;
drop table Content;
INSERT INTO Content(Content_id) VALUES (2);