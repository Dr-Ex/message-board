BEGIN TRANSACTION;

DELETE FROM users;
DELETE FROM messages;

INSERT INTO users VALUES(
	NULL,
	'tanya',
	'test',
	'Tanya',
	'Gray',
	'tanya@gathergather.co.nz',
	NULL
);
INSERT INTO messages VALUES (
	NULL,
	'Hello from tanya',
	datetime('now'),
	last_insert_rowid()
);

INSERT INTO users VALUES(
	NULL,
	'sarah',
	'password1',
	'Sarah',
	'Jones',
	'sarah@gathergather.co.nz',
	NULL
);
INSERT INTO messages VALUES (
	NULL,
	'Hello back, from Sarah',
	datetime('now'),
	last_insert_rowid()
);

INSERT INTO users VALUES(
	NULL,
	'pascal',
	'jack2014',
	'Pascal',
	'Black',
	'pascal@gathergather.co.nz',
	NULL
);
INSERT INTO messages VALUES (
	NULL,
	'Woof woof',
	datetime('now'),
	last_insert_rowid()
);

COMMIT;