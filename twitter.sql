create database CalebTwitter;
use CalebTwitter;
create table userInfor(
    id int AUTO_INCREMENT,
    created_at datetime,
    source varchar(511),
    original_text text,
    polarity float,
    subjectivity float,
    lang varchar(10),
    favorite_count int,
    retweet_count int,
    original_author varchar(250),
    followers_count int,
    friends_count int,
    possibly_sensitive varchar(250),
    hashtags varchar(250),
    user_mentions varchar(250),
    place varchar(50),
    primary key(id)
);