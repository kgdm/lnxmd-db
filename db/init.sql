GRANT ALL PRIVILEGES ON DATABASE lnxmd_dev TO postgres;

DROP TABLE IF EXISTS users_tb;

DROP TABLE IF EXISTS links_tb;

CREATE TABLE users_tb
(
    user_id INT 
    , user_name VARCHAR(50) UNIQUE NOT NULL
    , user_email VARCHAR(255)
    , user_passwd VARCHAR(32)
    , user_bio_pic VARCHAR(1000)
    , user_bio_link VARCHAR(1000)
    , PRIMARY KEY(user_id)
);

CREATE TABLE links_tb
(   link_id INT  NOT NULL PRIMARY KEY
    , link_user_id INT NOT NULL REFERENCES users_tb(user_id)
    , link_url VARCHAR(1000) NOT NULL
    , link_redirect_url VARCHAR(1000) NOT NULL
    , link_priority INT
    , link_added_on TIMESTAMP NOT NULL
    , link_expires_on TIMESTAMP
    , link_icon	VARCHAR(1000)
    , link_enabled BOOLEAN DEFAULT TRUE
    , link_highlight BOOLEAN DEFAULT TRUE
);
