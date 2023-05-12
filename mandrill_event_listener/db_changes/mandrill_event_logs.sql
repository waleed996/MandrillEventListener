CREATE TABLE mandrill_event_log(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   event_id TEXT NOT NULL, -- Should be unique but the id send in test events is the same by mandrill so not adding unique for now.
   type TEXT,
   data TEXT,
   created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);