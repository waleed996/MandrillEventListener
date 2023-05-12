from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ViewSet


class MandrillEventListenerViewSet(ViewSet):

    def dispatch(self, request, *args, **kwargs):
        """Override with custom logic, manipulate request headers, validate request body etc"""

        try:
            # Do any request manipulation
            # Validate request body etc

            self.headers = self.default_response_headers
            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            else:
                handler = self.http_method_not_allowed

            response = handler(request, *args, **kwargs)

        except Exception as err:
            # Log the error, can call our own custom exception handler to return custom response based
            # on our own Defined Exceptions
            response = self.handle_exception(err)

        return self.finalize_response(request, response, *args, **kwargs)


class PublicMandrillEventListenerViewSet(MandrillEventListenerViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]

