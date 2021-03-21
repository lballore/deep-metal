#!/bin/bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $SCRIPT_DIR/../src

OUTPUT_DIR=$SCRIPT_DIR/../deepmetal
TEST_FILE=$SCRIPT_DIR/../../datasets/deepmetal_test.txt

python run_language_modeling.py \
    --output_dir=$OUTPUT_DIR \
    --model_type=gpt2 \
    --model_name_or_path=$OUTPUT_DIR \
    --do_eval \
    --eval_data_file=$TEST_FILE \
    --per_device_eval_batch_size=3 \
    --gradient_accumulation_steps=5
