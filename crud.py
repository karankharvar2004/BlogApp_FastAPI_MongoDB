from datetime import datetime
from bson import ObjectId
from database import blog_collection

def blog_helper(blog) -> dict:
    return {
        "_id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
        "created_at": blog["created_at"],
    }


# GET ALL
async def get_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs


# CREATE
async def create_blog(blog):
    blog_dict = blog.dict()
    blog_dict["created_at"] = datetime.utcnow()

    result = await blog_collection.insert_one(blog_dict)
    new_blog = await blog_collection.find_one({"_id": result.inserted_id})

    return blog_helper(new_blog)


# GET ONE
async def get_blog(blog_id: str):
    blog = await blog_collection.find_one({"_id": ObjectId(blog_id)})
    if blog:
        return blog_helper(blog)
    return None


# UPDATE (PUT)
async def update_blog(blog_id: str, blog):
    await blog_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$set": blog.dict()}
    )

    updated = await blog_collection.find_one({"_id": ObjectId(blog_id)})
    if updated:
        return blog_helper(updated)
    return None


# PATCH
async def patch_blog(blog_id: str, blog):
    update_data = {k: v for k, v in blog.dict().items() if v is not None}

    await blog_collection.update_one(
        {"_id": ObjectId(blog_id)},
        {"$set": update_data}
    )

    updated = await blog_collection.find_one({"_id": ObjectId(blog_id)})
    if updated:
        return blog_helper(updated)
    return None


# DELETE
async def delete_blog(blog_id: str):
    result = await blog_collection.delete_one({"_id": ObjectId(blog_id)})
    return result.deleted_count == 1