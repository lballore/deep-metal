import random
from typing import Dict, List

from transformers import pipeline, set_seed
from transformers.pipelines.base import Pipeline


# to use GPU, set device=<CUDA_device_ordinal>
GENERATOR_MODEL = pipeline('text-generation', model='lucone83/deep-metal', device=-1)


def generate_lyrics(
    generator: Pipeline,
    text_inputs : str = "",
    max_length : int = 256,
    min_length : int = 128,
    top_p : float = 0.95,
    top_k : int = 50,
    temperature : float = 0.90
) -> List[Dict[str, str]]:

    set_seed(_generate_seed())
    lyrics = generator(
        text_inputs,
        max_length=max_length,
        min_length=min_length,
        top_p=top_p,
        top_k=top_k,
        temperature=temperature,
        num_return_sequences=1
    )

    return lyrics


def _generate_seed() -> int:
    return random.randint(1, 2147483647)
