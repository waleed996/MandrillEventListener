from threading import current_thread, local


def initialize_local_thread_storage():
    current_thread().local = local()
