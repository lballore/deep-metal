from typing import Dict, List

from transformers import pipeline, set_seed
from transformers.pipelines.base import Pipeline

from config import HyperParameters


# to use GPU, set device=<CUDA_device_ordinal>
GENERATOR_MODEL = pipeline('text-generation', model='lucone83/deep-metal', device=-1)


def generate_lyrics(
    generator: Pipeline,
    text_inputs: str,
    temperature: float
) -> List[Dict[str, str]]:

    lyrics = generator(
        text_inputs,
        temperature=temperature,
        do_sample=HyperParameters.DO_SAMPLE,
        bos_token_id=HyperParameters.BOS_TOKEN_ID,
        eos_token_id=HyperParameters.EOS_TOKEN_ID,
        top_k=HyperParameters.TOP_K,
        top_p=HyperParameters.TOP_P,
        num_return_sequences=HyperParameters.NUM_RETURN_SEQUENCES,
        no_repeat_ngram_size=_calculate_no_repeat_ngram_size(temperature),
        use_cache=HyperParameters.USE_CACHE
    )

    return lyrics


def _calculate_no_repeat_ngram_size(temperature: float) -> int:
    if temperature <= 0.65:
        return 3
    elif (temperature > 0.65 and temperature <= 0.85):
        return 6
    else:
        return 0
