import uuid

from threading import current_thread

from common.libs.thread import initialize_local_thread_storage


class UniqueRequestIdMiddleware:
    """Custom middleware to add a unique request_id in local storage for each request (to be used for scoped db session)"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        initialize_local_thread_storage()
        current_thread().local.request_id = uuid.uuid4().hex
        return self.get_response(request)
