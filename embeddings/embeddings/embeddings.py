from sentence_transformers import SentenceTransformer
import click
import pandas as pd
from tqdm import tqdm
from tqdm.contrib.concurrent import thread_map

# Create the model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Dummy function for now.
def calculate_embedding(text):
    # Add your actual implementation here
    return text


def process_record(record):
    record['overview'] = calculate_embedding(record['overview'])
    return record


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(input_file, output_file):
  # Read JSON line file
  df = pd.read_json(input_file, lines=True)
  # Take out
  breakpoint()
  sentences = df["overview"].values
  embeddings = model.encode(sentences)
  df["overview_embedding"] = embeddings
  # Write to new JSON line file
  df.to_json(output_file, orient='records', lines=True)

if __name__ == "__main__":
    main()
