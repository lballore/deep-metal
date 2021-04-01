import os

from transformers import TFGPT2Model

MODEL_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../deepmetal"

if __name__ == "__main__":
    tf_model = TFGPT2Model.from_pretrained(f"{MODEL_PATH}/", from_pt=True)
    tf_model.save_pretrained(f"{MODEL_PATH}/")
