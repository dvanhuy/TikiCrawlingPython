CREATE DATABASE pythonquanlylaptop;
use pythonquanlylaptop;
CREATE TABLE LapTop ( 
id VARCHAR(200) not null,
name_lap VARCHAR(2000) CHARSET utf8 not null,
brand_name VARCHAR(200) not null,
price VARCHAR(200), 
original_price VARCHAR(200) , 
discount VARCHAR(200), 
discount_rate VARCHAR(200),
rating_average VARCHAR(200), 
review_count VARCHAR(200),
thumbnail_url VARCHAR(200),
thumbnail_height VARCHAR(200), 
thumbnail_width VARCHAR(200),
video_url VARCHAR(200), 
seller_id VARCHAR(200),
PRIMARY KEY (id));


