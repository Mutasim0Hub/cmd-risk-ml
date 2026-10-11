import pandas as pd
import html
import glob

COMMAND_KEYS = ["command"]
LABEL_KEYS = ["label"]

def detect_column(columns, keywords):
    for col in columns:
        for key in keywords:
            if key in col:
                return col
    return None

def load_and_normalize(file_path):
    print(f"\n[INFO] Processing: {file_path}")

    df = pd.read_csv(file_path, sep=None, engine="python")
    df.columns = df.columns.astype(str).str.strip().str.lower()

    print(f"[INFO] Columns found: {list(df.columns)}")

    cmd_col = detect_column(df.columns, COMMAND_KEYS)
    label_col = detect_column(df.columns, LABEL_KEYS)

    if not cmd_col or not label_col:
        raise ValueError(f"[ERROR] Could not identify required columns in {file_path}")

    out = pd.DataFrame({
        "command": df[cmd_col].astype(str).apply(html.unescape).str.strip(),
        "label": df[label_col].astype(int),
    })

    return out

all_files = glob.glob("*.csv")
print("[INFO] CSV files detected:", all_files)

datasets = []
for f in all_files:
  
    if f == "data_clean.csv":
        continue
    datasets.append(load_and_normalize(f))

df = pd.concat(datasets, ignore_index=True)

df = df[df["command"] != ""]

df = df.drop_duplicates(subset=["command", "label"])
# حفظ
df.to_csv("data_clean.csv", index=False)
# تقارير
print("\n[INFO] Dataset Final is Ready")
print("[INFO] Label distribution:")
print(df["label"].value_counts())

print("\n[INFO] Sample rows:")
print(df.head())
