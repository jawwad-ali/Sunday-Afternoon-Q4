from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Pydantic models for request/response
class BlogCreate(BaseModel):
    title: str
    description: str

class Blog(BlogCreate):
    id: int

# In-memory storage
blogs_db: List[dict] = []
next_id = 1

app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:3000"],  # Adjust this for production
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
)

# Create a blog
@app.post("/api/blogs", response_model=Blog)
def create_blog(blog: BlogCreate):
    global next_id
    new_blog = {
        "id": next_id,
        "title": blog.title,
        "description": blog.description
    }
    blogs_db.append(new_blog)
    next_id += 1
    return new_blog

# Get all blogs
@app.get("/api/blogs", response_model=List[Blog])
def get_all_blogs():
    return blogs_db

# Get a single blog by ID
@app.get("/api/blogs/{blog_id}", response_model=Blog)
def get_blog(blog_id: int):
    for blog in blogs_db:
        if blog["id"] == blog_id:
            return blog
    raise HTTPException(status_code=404, detail="Blog not found")

# Update a blog
@app.put("/api/blogs/{blog_id}", response_model=Blog)
def update_blog(blog_id: int, blog: BlogCreate):
    for i, existing_blog in enumerate(blogs_db):
        if existing_blog["id"] == blog_id:
            blogs_db[i] = {
                "id": blog_id,
                "title": blog.title,
                "description": blog.description
            }
            return blogs_db[i]
    raise HTTPException(status_code=404, detail="Blog not found")

# Delete a blog
@app.delete("/api/blogs/{blog_id}")
def delete_blog(blog_id: int):
    for i, blog in enumerate(blogs_db):
        if blog["id"] == blog_id:
            deleted_blog = blogs_db.pop(i)
            return {"message": "Blog deleted successfully", "blog": deleted_blog}
    raise HTTPException(status_code=404, detail="Blog not found")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healty api"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
