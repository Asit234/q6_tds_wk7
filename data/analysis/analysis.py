# analysis/analysis.py
"""
CAC quarterly analysis script.
Generates:
 - analysis/outputs/cac_trend.png
 - analysis/outputs/cac_trend_with_benchmark.png
 - prints summary
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# --- Configuration ---
DATA_PATH = os.path.join("..", "data", "quarterly_cac.csv")  # if run from analysis/ folder
OUT_DIR = "outputs"
os.makedirs(OUT_DIR, exist_ok=True)

# Industry benchmark target
INDUSTRY_TARGET = 150.0

# --- Load data ---
df = pd.read_csv(DATA_PATH)
# Validate expected structure
if set(["quarter", "cac"]) - set(df.columns):
    raise ValueError("Input CSV must contain columns 'quarter' and 'cac'")

# Ensure quarters stay in order Q1..Q4
quarter_order = ["Q1", "Q2", "Q3", "Q4"]
df['quarter'] = pd.Categorical(df['quarter'], categories=quarter_order, ordered=True)
df = df.sort_values('quarter').reset_index(drop=True)

# --- Metrics ---
df['cac'] = df['cac'].astype(float)
total = df['cac'].sum()
average = total / len(df)
# Use requested display average (rounded to 2 decimals) but keep precise value
display_average = round(average, 2)

min_q = df.loc[df['cac'].idxmin()]
max_q = df.loc[df['cac'].idxmax()]

# --- Print summary ---
summary = f"""
Customer Acquisition Cost (CAC) quarterly summary
-----------------------------------------------
Quarters analyzed: {len(df)}
Quarter CAC values: {', '.join(df['quarter'] + ': ' + df['cac'].map(lambda x: f'{x:.2f}'))}
Average CAC (computed): {average:.4f}
Average CAC (rounded/display): {display_average}
Minimum CAC: {min_q['quarter']} = {min_q['cac']:.2f}
Maximum CAC: {max_q['quarter']} = {max_q['cac']:.2f}
Industry target: {INDUSTRY_TARGET:.2f}
"""
print(summary)

# --- Plots ---

# 1) Simple trend line
plt.figure(figsize=(8,4))
plt.plot(df['quarter'], df['cac'], marker='o')
plt.title("Quarterly CAC Trend (2024)")
plt.xlabel("Quarter")
plt.ylabel("CAC (currency units)")
plt.grid(True)
plt.tight_layout()
trend_path = os.path.join(OUT_DIR, "cac_trend.png")
plt.savefig(trend_path)
plt.close()
print(f"Saved trend plot to {trend_path}")

# 2) Trend with industry target and average
plt.figure(figsize=(8,4))
plt.plot(df['quarter'], df['cac'], marker='o', label='Quarterly CAC')
plt.hlines(INDUSTRY_TARGET, xmin=-0.5, xmax=3.5, linestyles='--', label=f'Industry Target = {INDUSTRY_TARGET:.0f}')
plt.hlines(average, xmin=-0.5, xmax=3.5, linestyles='-.', label=f'Average CAC = {display_average:.2f}')
plt.title("Quarterly CAC vs Industry Target (2024)")
plt.xlabel("Quarter")
plt.ylabel("CAC (currency units)")
plt.legend()
plt.grid(True)
plt.tight_layout()
trend_bench_path = os.path.join(OUT_DIR, "cac_trend_with_benchmark.png")
plt.savefig(trend_bench_path)
plt.close()
print(f"Saved benchmark plot to {trend_bench_path}")

# 3) Output a small csv summary
summary_df = pd.DataFrame({
    'metric': ['total', 'average', 'min_quarter', 'min_value', 'max_quarter', 'max_value', 'industry_target'],
    'value': [total, average, min_q['quarter'], min_q['cac'], max_q['quarter'], max_q['cac'], INDUSTRY_TARGET]
})
summary_csv_path = os.path.join(OUT_DIR, "summary_metrics.csv")
summary_df.to_csv(summary_csv_path, index=False)
print(f"Saved summary CSV to {summary_csv_path}")
