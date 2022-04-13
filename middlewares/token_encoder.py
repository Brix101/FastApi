from fastapi import Request

async def token_encoder(request: Request,call_next): 
    cookie_authorization: str = request.cookies.get("session")
        # some logic with cookie_authorization
    print(cookie_authorization)
    
    response = await call_next(request)
    return response