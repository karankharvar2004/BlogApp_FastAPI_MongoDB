from fastapi import APIRouter, HTTPException
import schemas
import crud

router = APIRouter()


@router.get("/blogs/", response_model=list[schemas.BlogResponse])
async def get_blogs():
    return await crud.get_blogs()


@router.post("/blogs/", response_model=schemas.BlogResponse)
async def create_blog(blog: schemas.BlogCreate):
    return await crud.create_blog(blog)


@router.get("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def get_blog(blog_id: str):
    blog = await crud.get_blog(blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@router.put("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def update_blog(blog_id: str, blog: schemas.BlogCreate):
    updated = await crud.update_blog(blog_id, blog)
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated


@router.patch("/blogs/{blog_id}", response_model=schemas.BlogResponse)
async def patch_blog(blog_id: str, blog: schemas.BlogUpdate):
    updated = await crud.patch_blog(blog_id, blog)
    if not updated:
        raise HTTPException(status_code=404, detail="Blog not found")
    return updated


@router.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: str):
    deleted = await crud.delete_blog(blog_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Blog not found")
    return {"message": "Deleted successfully"}