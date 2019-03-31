BEGIN TRANSACTION;

DROP TABLE IF EXISTS players;

CREATE TABLE players(
    id VARCHAR(20) PRIMARY KEY,
    uri TEXT
);

INSERT INTO players VALUES('kika', 'plugin://plugin.video.kikamediathek/?url=%s');
INSERT INTO players VALUES('youtube', 'plugin://plugin.video.youtube/play/?video_id=%s');
INSERT INTO players VALUES('netflix', 'plugin://plugin.video.netflix/?action=play_video&video_id=%s');
INSERT INTO players VALUES('prime', 'plugin://plugin.video.amazon-test/?asin=%s&mode=PlayVideo');


DROP TABLE IF EXISTS movies;

CREATE TABLE movies(
    id VARCHAR(10) PRIMARY KEY,
    description VARCHAR(255),
    player VARCHAR(20),
    c_id VARCHAR(255),
        FOREIGN KEY (player) REFERENCES players(id)
);

INSERT INTO movies VALUES('schief', 'das ist gerade', 'youtube', 'rJWZhitXWzI');
INSERT INTO movies VALUES('shaun1', 'eiskalte umleitung', 'netflix', '81022658');
INSERT INTO movies VALUES('shaun2', 'sackgasse', 'netflix', '80135565');
INSERT INTO movies VALUES('cars', 'cars 1', 'prime', 'B00IK9H632');
INSERT INTO movies VALUES('cars3', 'cars 3', 'prime', 'B075Y7C1RH');
INSERT INTO movies VALUES('benjamin', 'benjamin blümchen', 'prime', 'B0184UD7HA');
INSERT INTO movies VALUES('rollo', 'rollo rollt', 'youtube', '6qjREYDMzTU');

COMMIT;