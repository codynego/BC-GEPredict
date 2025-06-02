import pandas as pd

# Load the series matrix
series_matrix = pd.read_csv("data/GSE96058-GPL11154_series_matrix.txt", sep="\t", skiprows=63, header=None)
print(series_matrix.columns)