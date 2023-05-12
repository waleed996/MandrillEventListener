from threading import current_thread


def get_current_request_id():
    return getattr(current_thread().local, 'request_id', None)
