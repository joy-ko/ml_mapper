import os

cg_train_data_src = '/Users/ssom/Documents/mapper_dataset/cg_train'

def make_train_data(path_wt_name):
    train_header = []
    if os.path.exists(path_wt_name):
        pass
    else:
        with open(path_wt_name, "a") as f:
            f.write('\t'.join(train_header))

def add_train_tsv_row(path_wt_name, content):
    with open(path_wt_name, "a") as f:
        f.write(content)

