import os

from transformers import GPT2Config, TFGPT2LMHeadModel

MODEL_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../deepmetal"

if __name__ == "__main__":
    config = GPT2Config.from_pretrained(MODEL_PATH)
    tf_model = TFGPT2LMHeadModel.from_pretrained(f"{MODEL_PATH}/pytorch_model.bin", from_pt=True, config=config)
    tf_model.save_pretrained(MODEL_PATH)
