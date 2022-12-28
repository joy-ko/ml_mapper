import os, json

cg_labeled_data_src = "/Users/ssom/Documents/mapper_dataset/cg"

def load_labeled_json(path_wt_name):
    with open(path_wt_name, "r") as f:
        result = json.load(f)
    return result

def get_labeled_files(src):
    labeled_files = [f for f in os.listdir(src) if f.rsplit(".", maxsplit=1)[-1] == "json"]
    return labeled_files

