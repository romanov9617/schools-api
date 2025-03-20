from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.status import HTTP_404_NOT_FOUND


class NotFoundException(APIException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = {"Not found"}


def error404():
    raise NotFoundException()


class FieldIsRequiredException(APIException):
    status_code = HTTP_400_BAD_REQUEST
