from common.libs.db import db_session
from mandrill_event_listener.models.email_action import MandrillEventLog


class MandrillEventLogRepository:

    @staticmethod
    def create_mandrill_event_log(event_id, type, data, commit=True):
        mandrill_event_log = MandrillEventLog(event_id=event_id, type=type, data=str(data))

        # Add new obj to db_session
        db_session.add(mandrill_event_log)

        # Save or flush
        if commit:
            db_session.commit()
        else:
            db_session.flush()

