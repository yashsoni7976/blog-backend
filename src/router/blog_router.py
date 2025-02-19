from fastapi import APIRouter, Depends, HTTPException
from src.dependencies.get_db import get_db
from src.controller import blog_controller
from src.schemas.blog_schema import BlogCreateSchema, BlogUpdateSchema 

router = APIRouter()

@router.get("/")
def get_all_blogs_route(db=Depends(get_db)):
    return blog_controller.get_all_blogs(db)


@router.get("/{id}")
def get_blog_by_id_route(id: int, db=Depends(get_db)):
    return blog_controller.get_blog_by_id(db, id)


@router.post("/")
def create_blog_route(req:BlogCreateSchema, db=Depends(get_db)):
    if not req.title or not req.content:
        raise HTTPException(status_code=400, detail="Title and Content are required")
    return blog_controller.create_blog(req, db)


@router.put("/{id}")
def update_blog_route(id: int, req: BlogUpdateSchema, db=Depends(get_db)):
    return blog_controller.update_blog(id, req, db)


@router.delete("/{id}")
def delete_blog_route(id: int, db=Depends(get_db)):
    return blog_controller.delete_blog(id,db)