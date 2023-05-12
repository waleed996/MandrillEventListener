from sqlalchemy import Column, Integer, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base


# Base model definition, which will be part of all models and tables
class MandrillEventListenerBaseModel(object):
    id = Column(Integer, primary_key=True)
    created = Column(TIMESTAMP, server_default=func.now())
    updated = Column(TIMESTAMP, server_default=func.now(), server_onupdate=func.current_timestamp())


# Base Model declaration
MandrillBaseModel = declarative_base(cls=MandrillEventListenerBaseModel)
