sqlite3 farmers_markets
CREATE TABLE fmFeedback (
fmid Integer primary key,
market_name varchar(30)
);
.mode csv
.import fm.csv fmMetadata
