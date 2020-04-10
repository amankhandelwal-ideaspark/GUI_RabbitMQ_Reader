CREATE TABLE IF NOT EXISTS queue_details
(
ipurl text not null,
port text,
virtual_host text,
uname text,
pword text,
queue_name text
);
ALTER Table queue_details ADD COLUMN alias TEXT;