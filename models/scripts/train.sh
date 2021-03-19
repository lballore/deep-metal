#!/bin/bash

set -euxo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $SCRIPT_DIR/../src

OUTPUT_DIR=$SCRIPT_DIR/../deepmetal-medium
TRAIN_FILE=$SCRIPT_DIR/../../datasets/deepmetal_train.txt
VALIDATION_FILE=$SCRIPT_DIR/../../datasets/deepmetal_val.txt

python run_language_modeling.py \
    --output_dir=$OUTPUT_DIR \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --train_data_file=$TRAIN_FILE \
    --do_eval \
    --eval_data_file=$VALIDATION_FILE \
    --per_device_train_batch_size=3 \
    --per_device_eval_batch_size=3 \
    --evaluate_during_training \
    --learning_rate=1e-5 \
    --num_train_epochs=10 \
    --logging_steps=3000 \
    --save_steps=3000 \
    --gradient_accumulation_steps=5 \
    #--overwrite_output_dir  # uncomment if you want to continue training from last checkpoint
