from abc import ABC, abstractmethod

from mandrill_event_listener.repositories.mandrill_event_log_repository import MandrillEventLogRepository


class MandrillEventBaseComponent(ABC):

    @abstractmethod
    def handle(self, data):
        pass

    def save_event(self, event_type, event_id, event_data):
        """Generic base method in case there are multiple types of events"""
        MandrillEventLogRepository.create_mandrill_event_log(type=event_type,
                                                             event_id=event_id,
                                                             data=event_data)

