"""Preprocessing for EM-DAT Natural Disasters Emergency Events Database (Country Profiles).

Source: data/_EmergencyEventsDatabase-CountryProfiles_emdat-country-profiles_2023_04_06.csv
Output: data/emdat_cleaned.csv (comma-delimited, Tableau-ready)
"""
import pandas as pd

RAW_PATH = "data/_EmergencyEventsDatabase-CountryProfiles_emdat-country-profiles_2023_04_06.csv"
OUT_PATH = "data/emdat_cleaned.csv"

df = pd.read_csv(RAW_PATH, sep=";")

# Standardize column names (no spaces/commas, easier for Tableau field refs)
df.columns = [c.strip() for c in df.columns]
df = df.rename(columns={
    "Disaster Subroup": "Disaster Subgroup",  # fix source typo
    "Extreme temperature ": "Extreme temperature",
})

# CPI is stored as a string with a comma decimal separator (e.g. "2,8490844088613")
df["CPI"] = df["CPI"].astype(str).str.replace(",", ".", regex=False)
df["CPI"] = pd.to_numeric(df["CPI"], errors="coerce")

# Fix stray trailing space in Disaster Type category
df["Disaster Type"] = df["Disaster Type"].str.strip()

# Missing-value handling:
# - Total Affected / Total Deaths / Damage columns: leave as NaN (do not impute).
#   Charts using these fields should filter nulls explicitly rather than treating
#   missing as zero, since zero and "not reported" are not the same thing here.
# - Disaster Subtype: leave as NaN, label as "Not specified" only for display purposes.
df["Disaster Subtype"] = df["Disaster Subtype"].fillna("Not specified")

# Flag records before 1980 as lower-confidence for reporting completeness
df["Reporting Era"] = df["Year"].apply(lambda y: "Pre-1980 (sparse reporting)" if y < 1980 else "1980-present")

df.to_csv(OUT_PATH, index=False)
print(f"Wrote {len(df)} rows to {OUT_PATH}")
print(df.isna().sum())
