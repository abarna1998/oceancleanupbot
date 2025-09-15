from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import io
from .vision import detect_pollution
from services.openai_integration import summarize_report

app = FastAPI(title="Ocean Cleanup Bot API")

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content)).convert("RGB")
    # call detection (placeholder)
    detections = detect_pollution(image)  # returns list of dicts
    
    # create a small human-friendly summary using OpenAI (optional)
    summary = summarize_report(detections)
    
    return JSONResponse({"detections": detections, "summary": summary})

@app.get("/navigate")
def navigate(target: str = "hotspot"):
    from .navigation import navigate_to
    route = navigate_to(target)
    return {"route": route}
