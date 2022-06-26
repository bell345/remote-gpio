from pydantic import BaseModel
from starlette.responses import JSONResponse


class GenericException:
    _status_code = 400
    _default_msg = 'Error'
    detail: str

    @classmethod
    def response(cls, detail, **kwargs):
        if detail:
            kwargs['detail'] = detail
        else:
            kwargs['detail'] = cls._default_msg
        assert issubclass(cls, (BaseModel, GenericException))
        return JSONResponse(
                status_code=cls._status_code,
                content=cls(**kwargs).dict())


class NotFound(GenericException, BaseModel):
    _status_code = 404
    _default_msg = 'Not Found'


class BadRequest(GenericException, BaseModel):
    _status_code = 400
    _default_msg = 'Bad Request'


class Forbidden(GenericException, BaseModel):
    _status_code = 403
    _default_msg = 'Forbidden'


class TooLarge(GenericException, BaseModel):
    _status_code = 413
    _default_msg = 'Too Large'


class UnsupportedMediaType(GenericException, BaseModel):
    _status_code = 415
    _default_msg = 'Unsupported Media Type'

