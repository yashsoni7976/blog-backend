from fastapi import HTTPException
from src.models.blog_model import BlogModel
from src.models.user_model import UserModel

def get_all_blogs(db):
    blogs = db.query(BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=404, detail="No blogs found")
    return blogs


def get_blog_by_id(db, id: int):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


def create_blog(req, db):
    user = db.query(UserModel).filter(UserModel.id == req.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="The user and blog does not exist")
    blog = BlogModel(title=req.title, content=req.content, user_id=req.user_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def delete_blog(id,db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    db.delete(blog)
    db.commit()
    raise HTTPException(status_code=200, detail="Blog deleted successfully")


def update_blog(id, req, db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog.title = req.title
    blog.content = req.content
    db.commit()
    db.refresh(blog)
    return blog