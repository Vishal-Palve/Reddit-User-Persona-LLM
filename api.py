from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from app.reddit_scraper import scrape_user_data
from app.llm_analyzer import generate_persona

app = FastAPI(title="Reddit Persona Generator API")

@app.get("/generate_persona")
def generate(username: str = Query(..., description="Reddit username")):
    try:
        data = scrape_user_data(username)
        persona = generate_persona(data)
        return JSONResponse(content={"username": username, "persona": persona})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
