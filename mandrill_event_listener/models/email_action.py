from sqlalchemy import Column, TEXT

from mandrill_event_listener.models import MandrillBaseModel


class MandrillEventLog(MandrillBaseModel):
    __tablename__ = 'mandrill_event_log'

    event_id = Column(TEXT, nullable=False)
    type = Column(TEXT, nullable=True)
    data = Column(TEXT, nullable=True)

