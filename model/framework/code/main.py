# imports
import os
import csv
import sys
import joblib
import numpy as np
from FPSim2 import FPSim2Engine

# variables
FP_NAMES = [
    "morgan_2048",
    "maccs_166",
    "rdkit_2048",
    "atompair_2048",
    "pattern_2048"
]

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
checkpoints_dir = os.path.join(root, '..', '..', 'checkpoints')

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles_list = [r[0] for r in reader]

lr_model = joblib.load(os.path.join(checkpoints_dir, "logistic_regression.joblib"))

def get_X(smiles_list):
    R = []
    headers = []
    for fp_name in FP_NAMES:
        print(f"Processing fingerprint: {fp_name}")
        db_path = os.path.join(
            checkpoints_dir,
            f"{fp_name}.h5"
        )
        fpe = FPSim2Engine(db_path)
        k1s = []
        k3s = []
        k = 3
        idx_1 = 0
        idx_3 = 2
        for smiles in smiles_list:
            try:
                result = fpe.top_k(smiles, k=k, threshold=0.0, metric='tanimoto', n_workers=1)
                k1s += [float(result[idx_1][1])]
                k3s += [float(result[idx_3][1])]
            except Exception:
                k1s += [None]
                k3s += [None]
        R += [k1s, k3s]
        headers += [f"{fp_name}_k1", f"{fp_name}_k3"]
    X = np.array(R, dtype=float).T
    return X

# run
X = get_X(smiles_list)

# track which molecules have any NaN (failed) so we can emit empty rows for them
failed = np.any(np.isnan(X), axis=1)

outputs = [None] * len(smiles_list)
valid_indices = [i for i in range(len(smiles_list)) if not failed[i]]
if valid_indices:
    X_valid = X[valid_indices]
    preds = lr_model.predict_proba(X_valid)[:, 1].tolist()
    for idx, pred in zip(valid_indices, preds):
        outputs[idx] = pred

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["abx_score"])
    for o in outputs:
        if o is None:
            writer.writerow([""])
        else:
            writer.writerow([o])
