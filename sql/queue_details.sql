CREATE TABLE IF NOT EXISTS queue_details
(
id int AUTOINCREMENT,
ipurl text not null,
port text,
virtual_host text,
uname text,
pword text,
queue_name text
)