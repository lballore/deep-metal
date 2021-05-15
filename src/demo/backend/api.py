from typing import List, Dict

from fastapi import APIRouter, HTTPException, Header

from libs.deepmetal import GENERATOR_MODEL, generate_lyrics

API_VERSION = "v1"

def make_api_router(settings):
    app = APIRouter()


    @app.get("/test")
    def test():
        return "Test"


    @app.post("/generate")
    def generate(
        text_inputs : str = "",
        max_length : int = 256,
        min_length: int = 128,
        top_p : float = 0.95,
        top_k: int = 50,
        temperature : float = 0.90
     ) -> List[Dict[str, str]]:

        return generate_lyrics(
            generator=GENERATOR_MODEL,
            text_inputs=text_inputs,
            max_length=max_length,
            min_length=min_length,
            top_p=top_p,
            top_k=top_k,
            temperature=temperature
        )


    return app
