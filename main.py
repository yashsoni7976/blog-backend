from fastapi import FastAPI, Depends
from src.database.db_config import engine
from src.models import user_model, auth_model, blog_model
from src.router import user_router, auth_router, blog_router
from src.middleware.auth_middleware import get_current_user


user_model.Base.metadata.create_all(bind=engine)
auth_model.Base.metadata.create_all(bind=engine)
blog_model.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(user_router.router, prefix="/api/v1/user", tags=["user"], dependencies=[Depends(get_current_user)])
app.include_router(blog_router.router, prefix="/api/v1/blog", tags=["blog"], dependencies=[Depends(get_current_user)])
app.include_router(auth_router.router, prefix="/api/v1/auth", tags=["auth"])


@app.get("/")
def read_root():
    return {"Hello": "World"}
