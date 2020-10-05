import logging

from django.http import JsonResponse
from django.conf import settings

logger = logging.getLogger('django')

def exception_response(exception):
    '''
    Takes an exception and returns a JSON Response containing error details
    '''

    response = {}
    response['status_code'] = 500

    if settings.DEBUG or 1:
        response['data'] = {
            'exception_type': exception.__class__.__name__,
            'exception_message': str(exception),
            'exception_description': exception.__doc__
        }
    else:
        response['data'] = 'Error occured during execution.'

    logger.exception(response['data'])
    return response

def JsonResponseDecorator(view):
    '''
    Converts any data returned by a function into a JSON Response format.
    '''

    def wrapper(*args, **kwargs):

        try:
            response = view(*args, **kwargs)
        except Exception as e:
            response = exception_response(e)

        response = regularize_response(response)
        return JsonResponse(response)

    return wrapper
