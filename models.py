from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app
from slugify import slugify

db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('Kategoriya nomi', db.String(255))
    

class News(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('Sarlavha', db.String(255))
    slug = db.Column("Slug", db.String(255))
    content = db.Column('Mazmuni', db.Text)
    datetime = db.Column('Sana', db.DateTime, default=datetime.now)
    views = db.Column("Ko'rishlar soni", db.Integer, default=0)
    is_published = db.Column("Chop etilishi", db.Boolean)
    photo = db.Column("Muqova rasmi",db.String(255))
    
    cat_id = db.Column(db.Integer,db.ForeignKey("category.id"),nullable = True)

    def __init__(self, *args, **kwargs):

        if not "slug" in kwargs and "title"in kwargs:
            kwargs["slug"] = slugify(kwargs["title"])
        
        super().__init__(*args, **kwargs)


if __name__ == "__main__":
    db.create_all()