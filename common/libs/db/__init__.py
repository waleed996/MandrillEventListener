from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from common.libs.request_handler import get_current_request_id
from mandrill_event_listener_config.settings.base import BASE_DIR

# Create database engine
engine = create_engine('sqlite:///' + str(BASE_DIR) + '/mandrill_event_listener_db.sqlite3')

# Create a session factory
db_session = scoped_session(sessionmaker(bind=engine), scopefunc=get_current_request_id)

