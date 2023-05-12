from rest_framework.response import Response


def api_response(data, status_code=None):
    """Generic response method, to be used in the entire project for consistency"""

    return Response(data=data, status=status_code)
