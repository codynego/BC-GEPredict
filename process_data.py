import pandas as pd
import csv

# Load the series matri


def read_data():
    data_csv = {}
    with open('data/GSE96058-GPL11154_series_matrix.txt', 'r') as file:
        content = file.read().split("\n")
        for data in content:
            data_split = data.split('\t')
            data_split = [data.strip('"') for data in data_split]
            if len(data_split) < 3:
                continue
            data_csv[data_split[0]] =  data_split[1:]
        return data_csv

def convert_to_csv(data):
    with open("clinical_target.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerows(zip(*data.values()))
        # for key, value in data.items():
        #     writer.writerow([key, value])

def main():
    df = pd.read_csv('data/GSE96058_gene_expression_3273_samples_and_136_replicates_transformed.csv')
    print(df.iloc(1)) # Show the first 5 rows

main()        


