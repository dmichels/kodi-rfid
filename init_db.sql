BEGIN TRANSACTION;

DROP TABLE IF EXISTS players;

CREATE TABLE players(
    id VARCHAR(20) PRIMARY KEY,
    uri TEXT
);

INSERT INTO players VALUES('kika', 'plugin://plugin.video.kikamediathek/?url=%s');
INSERT INTO players VALUES('youtube', 'plugin://plugin.video.youtube/play/?video_id=%s');


DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    id VARCHAR(10) PRIMARY KEY,
    description VARCHAR(255),
    player VARCHAR(20),
    c_id VARCHAR(255),
        FOREIGN KEY (player) REFERENCES players(id)
);

INSERT INTO movies VALUES('cars', 'cars trailer', 'youtube', '2LeOH9AGJQM');
INSERT INTO movies VALUES('schief', 'das ist gerade', 'youtube', 'rJWZhitXWzI');
INSERT INTO movies VALUES('kika', 'irgendwas von kika', 'kika', 'http%3A%2F%2Fwww.kika.de%2Fvideo55606-avCustom.xml&mode=libMdrPlay');

COMMIT;