from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

import logging

log = logging.getLogger(__name__)


NOT_FOUND_VALIDATION = 'Http404'
DEFAULT_VALIDATION_FAILED = 'ValidationError'
SERVER_ERROR_MESSAGE = 'Ops. Server error'
FORBIDDEN_ERROR_MESSAGE = 'You do not have permission to perform this action.'


def pretty_errors_response(exc):
    """
    Custom error message depend on exception type
    @param exc:
    @return:
    """

    # Get exception class name
    exc_cls_name = exc.__class__.__name__
    errors = []

    if exc_cls_name == DEFAULT_VALIDATION_FAILED:
        for key, value in exc.detail.items():
            if isinstance(exc.get_codes()[key], list):
                errors.append({
                    'code_name': exc.get_codes()[key][0],
                    'field': key,
                    'message': value[0]
                })
            else:
                errors.append({
                    'code_name': exc.get_codes()[key][key],
                    'field': key,
                    'message': value[key]
                })
    elif exc_cls_name == NOT_FOUND_VALIDATION:
        pass
    else:
        errors.append({
            'code_name': exc.get_codes(),
            'message': exc.detail
        })

    return exc_cls_name, errors


def get_is_show_modal_error_field(errors):
    """
    Get is show modal error field in list errors
    @param errors: The list errors
    @return:
    """
    is_show_modal_error = None

    for error in errors:
        if error['field'] == 'is_show_modal_error':
            is_show_modal_error = bool(error['message'])
            break

    return is_show_modal_error


def custom_exception_handler(exc, context):
    """
    Call REST framework's default exception handler first,
    to get the standard error response.
    @param exc:
    @param context:
    @return:
    """

    response = exception_handler(exc, context)
    log.error(response)

    if not response:
        exc = APIException(exc)
        response = exception_handler(exc, context)

    exc_cls_name, errors = pretty_errors_response(exc)

    if response is not None:
        detail = response.data.get('detail')
        if detail:
            if response.status_code == 403:
                response.data['forbidden'] = {
                    'code': response.status_code,
                    'message': FORBIDDEN_ERROR_MESSAGE
                }

            response.data.pop('detail')
        else:
            [response.data.pop(key) for key in exc.get_codes().keys()]

            if response.status_code == 500:
                response.data['server_errors'] = {
                    'code': response.status_code,
                    'message': SERVER_ERROR_MESSAGE
                }

            if response.status_code == 400:
                response.data['validations'] = {}
                for err in errors:
                    response.data['validations'][f"{err['field']}"] = {
                        'code': response.status_code,
                        'field': err['field'],
                        'message': err['message']
                    }
    return response
