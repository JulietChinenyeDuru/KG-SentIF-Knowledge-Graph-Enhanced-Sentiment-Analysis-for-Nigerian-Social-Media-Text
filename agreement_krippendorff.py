# I recalculate Krippendorff's alpha between the two annotators from the published agreement sample

import sys
import numpy as np
import pandas as pd
import krippendorff
from importlib.metadata import version

FILE = sys.argv[1] if len(sys.argv) > 1 else "data/agreement_sample_200.csv"
df = pd.read_csv(FILE)

def alpha(a_values, b_values):
    clean = lambda x: "blank" if pd.isna(x) else str(x).strip()
    a_values = [clean(x) for x in a_values]
    b_values = [clean(x) for x in b_values]
    labels = sorted(set(a_values) | set(b_values))
    if len(labels) < 2:
        return float("nan")
    code = {label: i for i, label in enumerate(labels)}
    data = np.array([[code[x] for x in a_values], [code[x] for x in b_values]], dtype=float)
    return krippendorff.alpha(reliability_data=data, level_of_measurement="nominal")

def aspects(row, who):
    found = {}
    for i in (1, 2, 3):
        word = row[f"aspect{i}_{who}"]
        if pd.notna(word):
            found[str(word).strip().lower()] = (row[f"category{i}_{who}"], row[f"polarity{i}_{who}"])
    if pd.notna(row[f"implied_category_{who}"]):
        found["(implied)"] = (row[f"implied_category_{who}"], row[f"implied_polarity_{who}"])
    return found

results = []
for field in ["sarcastic", "cultural_reference", "language"]:
    results.append({"What": field, "Items": len(df),
                    "Alpha": alpha(df[f"{field}_annotator1"], df[f"{field}_annotator2"])})

matched, n1, n2, cat1, cat2, pol1, pol2 = 0, 0, 0, [], [], [], []
for _, row in df.iterrows():
    a, b = aspects(row, "annotator1"), aspects(row, "annotator2")
    n1 += len(a); n2 += len(b)
    for word in set(a) & set(b):
        matched += 1
        cat1.append(a[word][0]); cat2.append(b[word][0])
        pol1.append(a[word][1]); pol2.append(b[word][1])

precision, recall = matched / max(n2, 1), matched / max(n1, 1)
f1 = 2 * precision * recall / max(precision + recall, 1e-9)
results.append({"What": "category (aspects both marked)", "Items": matched, "Alpha": alpha(cat1, cat2)})
results.append({"What": "polarity (aspects both marked)", "Items": matched, "Alpha": alpha(pol1, pol2)})

table = pd.DataFrame(results)
table["Alpha"] = table["Alpha"].round(3)
print(f"krippendorff package version: {version("krippendorff")}")
print(table.to_string(index=False))
print(f"Aspect-word agreement F1 = {f1:.3f}")
