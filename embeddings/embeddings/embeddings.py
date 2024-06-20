from sentence_transformers import SentenceTransformer
import click
import pandas as pd

# Create the model
model = SentenceTransformer("all-MiniLM-L6-v2")


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def main(input_file, output_file):
  # Read JSON line file
  df = pd.read_json(input_file, lines=True)
  sentences = df["overview"].values
  embeddings = model.encode(sentences)
  df["overview_embedding"] = embeddings.tolist()
  # Write to new JSON line file
  df.to_json(output_file, orient='records', lines=True)

if __name__ == "__main__":
    main()
