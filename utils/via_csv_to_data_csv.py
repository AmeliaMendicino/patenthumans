"""
Creates a data.csv file from a VIA csv file in the format
name: uuid.png, [labels: 0|1, ...], url: string
"""
import argparse
import pandas as pd
import json
import uuid
import sys

parser = argparse.ArgumentParser()

parser.add_argument('--file', required=True,
                    help='The VIA csv file to convert to a data.csv')
parser.add_argument('--labels', required=True,
                    help='A comma seperated list of header labels')

args = parser.parse_args()
file = args.file
labels = args.labels.split(',')

df = pd.read_csv(file)

# Convert file_attributes json column into a dict
df['file_attributes'] = df['file_attributes'].apply(json.loads)

# Create DataFrames with dict comprehension to get the JSON
# file annotations as columns
df1 = pd.concat({k: pd.DataFrame(v)
                for k, v in df['file_attributes'].items()})
df = df.join(df1.reset_index(level=1, drop=True)).reset_index(drop=True)

# Get rid of all the NaN values
df = df.fillna(0)

# Rearrange the columns to only the ones we need
df = df[[c for c in df if c in labels]
        + ['filename']]
df = df.rename({'filename': 'url'}, axis='columns')

# Convert all the label column values to either 1 or 0
df = df.astype({c: int for c in labels})

# Give each row a random filename for reference when we download them later
filenames = [uuid.uuid4().hex + ".png" for _ in range(len(df.index))]
df.insert(loc=0, column='name', value=filenames)

# Save the DataFrame as a csv, converting all the 1.0 and 0.0's to ints
df.to_csv('data.csv', index=False, float_format="%.0f", header=True)
