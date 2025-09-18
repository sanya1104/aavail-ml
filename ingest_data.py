
import pandas as pd
import json
import glob

def load_json_data(path_pattern="data/*.json"):
    files = glob.glob(path_pattern)
    data_list = []
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
            data_list.extend(data)
    df = pd.DataFrame(data_list)
    return df
