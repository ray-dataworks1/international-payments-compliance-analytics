import pandas as pd
import glob
import os

data_dir = 'C:/Users/rogun/international-payments-compliance-analytics/data'
csv_files = glob.glob(os.path.join(data_dir, '*.csv'))

eli5_explanations = """
**ELI5: What do these columns mean?**
- **Data Type:** What kind of data is in this column? (numbers, text, dates, True/False, etc.)
- **Non-Null Count:** How many rows have *something* in this column? (Not empty)
- **Unique Values:** How many different values are there in this column?
- **Missing Values:** How many rows are blank/missing in this column?
- **Missing Percentage:** What percent of the rows are missing/blank?
- **Min/Max/Mean/Std:** Only for number columns—smallest/largest, average, and how much the numbers vary.
"""

md_lines = [
    "# Data Profiling Summary",
    "",
    eli5_explanations,
    "",
    "---"
]

excel_path = os.path.join(data_dir, 'data_profiles.xlsx')
with pd.ExcelWriter(excel_path) as writer:
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if df.empty:
                continue

            table_name = os.path.splitext(os.path.basename(file))[0]

            # Profiling metrics
            profile = pd.DataFrame({
                'Data Type': df.dtypes,
                'Non-Null Count': df.notnull().sum(),
                'Unique Values': df.nunique(),
                'Missing Values': df.isnull().sum(),
                'Missing Percentage': (df.isnull().sum() / len(df)) * 100
            })

            # Add numeric stats if any
            num_stats = df.describe().T if not df.select_dtypes(include='number').empty else pd.DataFrame()

            # Save to Excel (profile + numeric stats)
            profile.to_excel(writer, sheet_name=table_name[:31])
            if not num_stats.empty:
                # Write numeric stats just below profile in the same sheet
                startrow = len(profile) + 3
                num_stats.to_excel(writer, sheet_name=table_name[:31], startrow=startrow)

            # --- Markdown Section ---
            md_lines.append(f"## {table_name}")
            md_lines.append("")
            md_lines.append("| Column | Data Type | Non-Null Count | Unique Values | Missing Values | Missing % |")
            md_lines.append("|--------|-----------|---------------|---------------|---------------|-----------|")
            for idx, row in profile.iterrows():
                md_lines.append(
                    f"| {idx} | {row['Data Type']} | {row['Non-Null Count']} | {row['Unique Values']} | {row['Missing Values']} | {row['Missing Percentage']:.2f} |"
                )
            md_lines.append("")

            # Add numeric stats to markdown if present
            if not num_stats.empty:
                md_lines.append("**Numeric column stats:**")
                md_lines.append("")
                md_lines.append("| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |")
                md_lines.append("|--------|-------|------|-----|-----|-----|-----|-----|-----|")
                for idx, row in num_stats.iterrows():
                    md_lines.append(
                        f"| {idx} | {row['count']} | {row['mean']:.2f} | {row['std']:.2f} | {row['min']:.2f} | {row['25%']:.2f} | {row['50%']:.2f} | {row['75%']:.2f} | {row['max']:.2f} |"
                    )
                md_lines.append("")

            # --- ELI5 & Top-3 summary/warnings per table ---
            notes = []
            for idx, row in profile.iterrows():
                if row['Missing Percentage'] > 20:
                    notes.append(f"- **WARNING:** '{idx}' is {row['Missing Percentage']:.1f}% missing.")
                if row['Unique Values'] == profile.loc[idx, 'Non-Null Count'] and row['Missing Values'] == 0 and row['Data Type'] in ('int64', 'object'):
                    notes.append(f"- '{idx}' is unique—likely a primary key.")
                if row['Data Type'] == 'object' and row['Unique Values'] < 10 and row['Missing Percentage'] < 10:
                    notes.append(f"- '{idx}' is a categorical field with a small number of distinct values.")
            # ELI5 summary for table
            if not notes:
                notes = [f"- All columns have expected types and low missingness. No major issues detected."]
            md_lines.append("**What you need to know (ELI5):**")
            md_lines.extend(notes)
            md_lines.append("\n---")

        except Exception as e:
            md_lines.append(f"**ERROR processing {file}: {e}**")
            md_lines.append("---")

# Save markdown file
md_path = os.path.join(data_dir, "data_profile_summary.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write('\n'.join(md_lines))

print('Profiles saved to:')
print(f'- Excel: {excel_path}')
print(f'- Markdown: {md_path}')
