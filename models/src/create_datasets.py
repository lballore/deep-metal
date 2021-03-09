import argparse
import numpy as np
import pandas as pd
import os

from tqdm import tqdm

DATASETS_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/../../datasets"
TRAIN_RATIO = 0.7
EVAL_RATIO = 0.2
TEST_RATIO = 0.1


def build_dataset(df, dest_path, dataset_name='dataset'):
    print(f"Building {dataset_name} ({len(df)} documents) ...")
    f = open(dest_path, 'w')
    data = ''
    lyrics = df['lyrics'].tolist()
    for lyric in tqdm(lyrics):
        lyric = str(lyric).strip()
        lyric = lyric.replace("\\n", "\n")
        bos_token = '<|startoftext|>'
        eos_token = '<|endoftext|>'
        data += bos_token + ' ' + lyric + ' ' + eos_token + '\n'

    f.write(data)
    f.close()


def main(args):
    metal_lyrics_df = pd.read_csv(args.dataset, sep=args.separator)
    print(f"Number of documents: {len(metal_lyrics_df)}")

    assert round(TRAIN_RATIO + EVAL_RATIO, 1) == round(1.0 - TEST_RATIO, 1), "Invalid dataset proportions!"
    train, validate, test = np.split(
        metal_lyrics_df.sample(frac=1, random_state=666),  # shuffle
        [int(TRAIN_RATIO * len(metal_lyrics_df)),
         int(round(TRAIN_RATIO + EVAL_RATIO, 1) * len(metal_lyrics_df))]
    )

    build_dataset(train, f'{DATASETS_PATH}/deepmetal_train.txt', "train dataset")
    build_dataset(validate, f'{DATASETS_PATH}/deepmetal_val.txt', "evaluation dataset")
    build_dataset(test, f'{DATASETS_PATH}/deepmetal_test.txt', "test dataset")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dataset", type=str, help="Path of the lyrics dataset")
    parser.add_argument("-s", "--separator", type=str, default="|", help="Column separator of the dataset file")
    args = parser.parse_args()

    main(args)
