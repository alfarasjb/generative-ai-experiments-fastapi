from fastapi import FastAPI, Query, Response, status
from models import load_image_model, generate_image
from utils import img_to_bytes


app = FastAPI()


@app.get("/generate/image")
def serve_text_to_image_model_controller(prompt: str = Query(...)):
    pipe = load_image_model()
    output = generate_image(pipe, prompt)
    return Response(content=img_to_bytes(output), media_type="image/png")
