#!/bin/bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $SCRIPT_DIR/../src

OUTPUT_DIR=$SCRIPT_DIR/../deepmetal

python run_generation.py \
    --model_type=gpt2 \
    --model_name_or_path=$OUTPUT_DIR \
    --length=-1 \
    --prompt="<|startoftext|>" \
    --stop_token="<|endoftext|>" \
    --seed=$(echo $RANDOM) \
    --num_return_sequences=1 \
    --p=0.97 \
    --temperature=0.80 \
