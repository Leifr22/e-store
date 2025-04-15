from loguru import logger
from fastapi import FastAPI, Request
from uuid import uuid4
from fastapi.responses import JSONResponse

app=FastAPI()
logger.add('info.log', format="Log: [{extra[log_id]}:{time} - {level} - {message}]", level='INFO', enqueue= True)

async def log_middleware(request:Request, call_next):
    log_id=str(uuid4())
    with logger.contextualize(log_id=log_id):
        try:
            response= await call_next(request)
            if response.status_code in [401,402,403,404]:
                logger.warning(f'{request.url.path} - request failed')
            else:
                logger.info(f'Request {request.url.path} successful ')
        except Exception as ex:
            logger.error(f'Request to {request.url.path} failed: {ex}')
            response= JSONResponse(content={'success': False}, status_code=500)
        return response



