from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.scraper import scrape_all
from app.services.gen_ai import generate_portfolio
from app.utils.logger import logger

router = APIRouter()

class UserLinks(BaseModel):
    github: str | None = None
    medium: str | None = None
    leetcode: str | None = None
    linkedin: str | None = None
    twitter: str | None = None

@router.post("/generate")
async def generate_resume(user_links: UserLinks):
    try:
        logger.info(f"Github: {user_links.github}")
        logger.info(f"medium: {user_links.medium}")
        logger.info(f"leetcode: {user_links.leetcode}")
        logger.info(f"linkedin: {user_links.linkedin}")
        logger.info(f"twitter: {user_links.github}")

        raw_data = await scrape_all(user_links)
        result = await generate_portfolio(raw_data)
        return result
    except Exception as e:
        logger.error(f"Error generating resume: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))