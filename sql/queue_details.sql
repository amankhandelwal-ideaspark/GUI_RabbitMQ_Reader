CREATE TABLE IF NOT EXISTS queue_details
(
id int AUTO_INCREMENT,
ipurl text not null,
port text,
virtual_host text,
uname text,
pword text,
queue_name text
)